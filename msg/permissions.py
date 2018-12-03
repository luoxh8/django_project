from rest_framework.permissions import BasePermission

from msg.models import MsgHandler


class IsMsgReceiver(BasePermission):
    def has_object_permission(self, request, view, obj):
        mh = MsgHandler.objects.filter(msg_id=obj).first()
        if not mh:
            return False
        return mh.receiver == request.user
