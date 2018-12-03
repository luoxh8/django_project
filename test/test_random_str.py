import os
import random
import string


def randomString(n):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(n))))[0:16]


def gen_random_string(string_length):
    return ''.join(random.sample(string.ascii_letters + string.digits, string_length))


def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


print(id_generator(64))
