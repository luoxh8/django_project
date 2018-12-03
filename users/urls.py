from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from users.views import (ChangePasswordAPIView,
                         InfoAPIView,
                         PhoneLogin,
                         PhoneRegister,
                         ResetPasswordAPIView,
                         ThirdLoginAPIView)

urlpatterns = [
    path('phone/login', PhoneLogin.as_view()),  # 手机登录
    path('phone/register', PhoneRegister.as_view()),  # 手机注册
    path('login', ThirdLoginAPIView.as_view()),  # 第三方注册
    path('changePassword', ChangePasswordAPIView.as_view()),  # 修改密码
    path('resetPassword', ResetPasswordAPIView.as_view()),  # 重置密码
    path('info', InfoAPIView.as_view()),  # 用户信息
    path('tokenRefresh', refresh_jwt_token),  # 刷新token
]
