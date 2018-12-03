import re
from datetime import datetime

import requests
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from h_utils.generator import gen_ip, gen_random_string, gen_uid
from h_utils.response_extra import (err_base_params,
                                    err_user_does_exist,
                                    err_user_does_not_exist,
                                    err_user_not_access_the_validate,
                                    err_user_not_supported_for_login,
                                    err_user_password_incorrect,
                                    err_user_reset_password,
                                    err_user_same_password,
                                    success_request)
from h_utils.serializers_extra import serializer_data
from h_utils.success import dict_success, normal_success
from h_utils.validator import is_code, is_password, is_phone
from users.models import Balance, Profile
from users.serializers import ProfileSerializer


class PhoneRegister(APIView):

    @staticmethod
    def post(request):
        try:
            # get
            platform = request.query_params['platform']
            device_id = request.query_params['device_id']

            # post
            phone = request.data['phone']
            password = request.data['password']
            code = request.data['code']
        except KeyError:
            return err_base_params()

        if not is_phone(phone):
            return err_base_params()

        if not is_password(password):
            return err_base_params()

        if not is_code(code):
            return err_base_params()

        exists = Profile.objects.filter(phone=phone).exists()

        if exists:
            return err_user_does_exist()

        user = Profile.objects.create(uid=gen_uid(),
                                      phone=phone,
                                      password=make_password(password),
                                      platform=platform,
                                      username='手机用户' + phone,
                                      register_ip=gen_ip(request),
                                      device_id=device_id, )

        Balance.objects.create(
            user=user,
        )

        return_data = dict_success()
        return_data['msg'] = '注册成功'
        return_data['data'] = serializer_data(user, ProfileSerializer, request)
        return_data['data']['token'] = jwt_encode_handler(jwt_payload_handler(user))
        return success_request(return_data)


class PhoneLogin(APIView):

    @staticmethod
    def post(request):
        try:
            phone = request.data['phone']
            password = request.data['password']
        except KeyError:
            return err_base_params()

        if not is_phone(phone):
            return err_base_params()

        if not is_password(password):
            return err_base_params()

        user = Profile.objects.filter(phone=phone).first()

        if not user:
            return err_user_does_not_exist()

        if not check_password(password, user.password):
            return err_user_password_incorrect()

        return_data = dict_success()
        return_data['msg'] = '登录成功'
        return_data['data'] = serializer_data(user, ProfileSerializer, request)
        return_data['data']['token'] = jwt_encode_handler(jwt_payload_handler(user))
        return success_request(return_data)


class ThirdLoginAPIView(APIView):
    login_zone = ['sinaweibo', 'qzone', 'wechat']
    username = None

    def check_in_login_zone(self, oauth_from):
        if oauth_from not in self.login_zone:
            return False, err_user_not_supported_for_login()

    def validate_and_get_userinfo(self, oauth_from, access_token, oauth_openid):
        if oauth_from == self.login_zone[0]:
            ret = requests.get('https://api.weibo.com/2/users/show.json',
                               params={'access_token': access_token,
                                       'uid'         : int(oauth_openid)})
            ret = ret.json()
            self.username = '微博用户' + oauth_openid + gen_random_string()
            return ret.get('error_code', 0) == 0, ret
        elif oauth_from == self.login_zone[1]:
            ret = requests.get('https://graph.qq.com/user/get_user_info',
                               params={'access_token'      : access_token,
                                       'openid'            : oauth_openid,
                                       'oauth_consumer_key': '1106741162',
                                       'format'            : 'json'})
            ret = ret.json()
            self.username = 'qq用户' + oauth_openid + gen_random_string()
            return ret['ret'] == 0, ret
        elif oauth_from == self.login_zone[2]:
            ret = requests.get('https://api.weixin.qq.com/sns/userinfo',
                               params={'access_token': access_token,
                                       'openid'      : oauth_openid})
            ret = ret.json()
            self.username = '微信用户' + oauth_openid + gen_random_string()
            return ret.get('errcode', 0) == 0, ret

    def clear_nick(self, nick):
        name_group = []
        for c in nick:
            regex = r'^[( )(\u4e00-\u9fa5)(\u0030-\u0039)(\u0041-\u005a)(\u0061-\u007a)(' \
                    r'~！@#￥%…&（）—“”：？》《·=、】【‘’；、。，!_:`;/,<>})(\-\*\+\|\{\$\^\(\)\?\.\[\])]+$'
            if not re.match(regex, c):
                name_group.append('*')
            name_group.append(c)
        nick = ''.join(name_group)
        return nick

    def post(self, request):
        try:

            # get
            platform = request.query_params['platform']
            device_id = request.query_params['device_id']

            # post
            gender = request.data['gender']
            oauth_from = request.data['oauth_from']
            oauth_openid = request.data['open_id']
            access_token = request.data['token']
            nick = request.data['nick']
            avatar = request.data['avatar']

            gender = int(gender)

        except KeyError:
            return err_base_params()
        except ValueError:
            return err_base_params()

        is_in_login_zone, return_data = self.check_in_login_zone(oauth_from)
        if not is_in_login_zone:
            return return_data

        is_valid, oauth_userinfo = self.validate_and_get_userinfo(oauth_from, access_token, oauth_openid)

        if not is_valid:
            return err_user_not_access_the_validate()

        user = Profile.objects.filter(oauth_openid=oauth_openid).first()
        if user:
            return_data = dict_success()
            return_data['msg'] = '登录成功'
            return_data['data'] = serializer_data(user, ProfileSerializer, request)
            return_data['data']['token'] = jwt_encode_handler(jwt_payload_handler(user))
            return success_request(return_data)

        user = Profile.objects.create(uid=gen_uid(),
                                      username=self.username,
                                      nick=self.clear_nick(nick),
                                      register_ip=gen_ip(request),
                                      device_id=device_id,
                                      platform=platform,
                                      avatar=avatar,
                                      gender=gender,
                                      oauth_openid=oauth_openid,
                                      oauth_from=oauth_from,
                                      oauth_userinfo=oauth_userinfo,
                                      oauth_time=datetime.now())
        Balance.objects.create(
            user=user,
        )
        return_data = dict_success()
        return_data['msg'] = '登录成功'
        return_data['data'] = serializer_data(user, ProfileSerializer, request)
        return_data['data']['token'] = jwt_encode_handler(jwt_payload_handler(user))
        return success_request(return_data)


class InfoAPIView(APIView):
    permission_classes = (IsAuthenticated,) or (IsAdminUser,)

    @staticmethod
    def get(request):
        user = Profile.objects.filter(username=request.user).first()

        if not user:
            return err_user_does_not_exist()

        return_data = dict_success()
        return_data['data'] = serializer_data(user, ProfileSerializer, request)
        return success_request(return_data)


class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,) or (IsAdminUser,)

    @staticmethod
    def post(request):
        try:
            old_password = request.data['old_password']
            new_password = request.data['new_password']
        except KeyError:
            return err_base_params()

        if not is_password(new_password):
            return err_base_params()

        if old_password == new_password:
            return err_user_same_password()

        user = Profile.objects.filter(username=request.user).first()

        if not check_password(old_password, user.password):
            return err_user_password_incorrect()

        user.password = make_password(new_password)
        user.save()

        return_data = normal_success()
        return_data['msg'] = '修改成功'
        return success_request(return_data)


class ResetPasswordAPIView(APIView):

    @staticmethod
    def post(request):
        try:
            phone = request.data['phone']
            password = request.data['password']
            code = request.data['code']
        except KeyError:
            return err_base_params()

        if not is_code(code):
            return err_user_reset_password()

        user = Profile.objects.filter(phone=phone).first()
        user.password = make_password(password)
        user.save()

        return_data = normal_success()
        return_data['msg'] = '重置成功'
        return success_request(return_data)


class RechargeAPIView(APIView):
    permission_classes = (IsAuthenticated,) or (IsAdminUser,)

    @staticmethod
    def post(request):
        pass
