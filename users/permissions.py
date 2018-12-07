from rest_framework.permissions import BasePermission


class IsInfoSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        只在viewset的时候可以起作用
        :param request: 请求
        :param view: 视图
        :param obj: 对象
        :return:
        """
        return obj.username == request.user
