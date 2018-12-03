from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from h_utils.permissions import IsOwner
from h_utils.success import array_success
from user_operation.models import Collection


class FavoriteProductAPIView(APIView):
    permission_classes = (IsAuthenticated, IsOwner) or (IsAdminUser,)

    @staticmethod
    def get(request):
        collection_list = Collection.objects.filter(user__username=request.user).all()
        return_data = array_success()
        return_data['data'] = None
        return

    @staticmethod
    def post(request):
        pass
