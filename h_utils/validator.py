import re

from django.contrib.auth import get_user_model

from goods.models import Goods
from users.models import Profile

User = get_user_model()


def is_empty(value):
    return value is None


def is_phone(phone_number):
    if not phone_number or re.match('^1([34578]\d{9})$', phone_number) is None:
        return False
    return True


def is_goods_id(goods_id):
    return Goods.objects.filter(goods_id=goods_id).exists()


def is_uid(uid):
    return Profile.objects.filter(uid=uid).exists()


def is_code(code):
    return code == '66666'


def is_password(password):
    if not password or len(password) < 6 or len(password) > 30:
        return False
    else:
        return True
