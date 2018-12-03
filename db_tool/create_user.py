import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()

from django.contrib.auth.hashers import make_password
from h_utils.generator import gen_uid
from users.models import Profile, Balance

user = Profile.objects.create(uid=gen_uid(),
                              phone='15913538383',
                              password=make_password('huihui123'),
                              platform='ios',
                              username='手机用户' + '15913538383',
                              register_ip='0.0.0.0',
                              device_id=None)

Balance.objects.create(user=user,
                       balance=0.0,
                       total=0.0, )
print('user数据导入完成')
