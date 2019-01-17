from rest_framework import status
from rest_framework.response import Response


class ResponseExtra:

    @staticmethod
    def send_bad_response(e):
        return Response(e, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def send_ok_response(d):
        return Response(d, status=status.HTTP_200_OK)


# ==========
# 成功
# ==========
def success_request(data):
    return ResponseExtra.send_ok_response(data)


# ==========
# 错误
# ==========
def error_request(data):
    return ResponseExtra.send_bad_response(data)

#
# # bad request
# def err_sys_bad_request():
#     return error_request(ErrSysBadRequest)
#
#
# # 找不到页面
# def err_sys_page_not_found():
#     return error_request(ErrSysPageNotFound)
#
#
# # 找不到路由
# def err_sys_api_not_found():
#     return error_request(ErrSysApiNotFound)
#
#
# # 服务器内部错误
# def err_base_server():
#     return error_request(ErrBaseServer)
#
#
# # 参数错误
# def err_base_params():
#     return error_request(ErrBaseParams)
#
#
# # 暂无数据
# def err_base_not_data():
#     return error_request(ErrBaseNotData)
#
#
# # 暂无数据
# def err_base_illegal_permission():
#     return error_request(ErrBaseIllegalPermission)
#
#
# # 用户不存在
# def err_user_does_not_exist():
#     return error_request(ErrUserDoesNotExist)
#
#
# # 用户已经存在
# def err_user_does_exist():
#     return error_request(ErrUserDoesExist)
#
#
# # 密码错误
# def err_user_password_incorrect():
#     return error_request(ErrUserPasswordIncorrect)
#
#
# # 相同密码
# def err_user_same_password():
#     return error_request(ErrUserSamePassword)
#
#
# # 重置密码的验证码错误
# def err_user_reset_password():
#     return error_request(ErrUserResetPassword)
#
#
# # 不支持此方式登录
# def err_user_not_supported_for_login():
#     return error_request(ErrUserNotSupportedForLogin)
#
#
# # 信息没有通过验证
# def err_user_not_access_the_validate():
#     return error_request(ErrUserNotAccessTheValidate)
#
#
# # 暂无商品
# def err_goods_not_found():
#     return error_request(ErrGoodsNotFound)
#
#
# # 余额不足
# def err_goods_bid():
#     return error_request(ErrGoodsBid)
#
#
# # 正在出价
# def err_goods_bidding():
#     return error_request(ErrGoodsBidding)
