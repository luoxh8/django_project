import random
import string

from h_utils.validator import is_goods_id, is_uid


def gen_random_string(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def gen_uid():
    zero_to_nine = string.digits
    one_to_nine = zero_to_nine[1:]

    def _uid():
        first = gen_random_string(1, one_to_nine)
        others = gen_random_string(6, zero_to_nine)
        return first + others

    while True:
        uid = _uid()
        if not is_uid(uid):
            return uid


def gen_goods_id():
    while True:
        goods_id = gen_random_string(64)
        if not is_goods_id(goods_id):
            return goods_id


def gen_ip(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip
