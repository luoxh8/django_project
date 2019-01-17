from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from h_utils.errors import ErrBaseNotData, ErrBaseParams, ErrBaseIllegalPermission
from h_utils.response_extra import success_request, error_request
from h_utils.success import array_success, dict_success
from msg.models import Msg, MsgHandler
from msg.permissions import IsMsgReceiver
from msg.serializers import MsgListSerializer, MsgSerializer


class MsgAPIView(APIView):
    permission_classes = (IsAuthenticated,) or (IsAdminUser,)

    @staticmethod
    def get(request):
        msg_array = []
        msg_list = MsgHandler.objects.filter(receiver__username=request.user.username).all()

        for msg in msg_list:
            msg_array.append(Msg.objects.filter(pk=msg.msg_id).first())

        if not msg_array:
            return error_request(ErrBaseNotData)

        return_data = array_success()
        return_data['data'] = (MsgListSerializer(value).data for value in msg_array)
        return success_request(return_data)


class MsgDetailAPIView(APIView):
    permission_classes = (IsAuthenticated, IsMsgReceiver) or (IsAdminUser,)

    def get(self, request):
        try:
            msg_id = request.query_params['msg_id']
        except KeyError:
            return error_request(ErrBaseParams)

        msg = Msg.objects.filter(pk=msg_id).first()

        if not msg:
            return error_request(ErrBaseNotData)

        if self.check_object_permissions(request, msg_id):
            return error_request(ErrBaseIllegalPermission)

        return_data = dict_success()
        return_data['data'] = MsgSerializer(msg).data
        return success_request(return_data)
