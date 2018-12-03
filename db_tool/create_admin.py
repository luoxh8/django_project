import os
import sys

from django.contrib.auth.hashers import make_password

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()
from users.models import Profile, Balance
from h_utils.generator import gen_uid

user = Profile.objects.create(uid=gen_uid(),
                              username='admin',
                              password=make_password('huihui123'),
                              is_superuser=True,
                              is_staff=True)

Balance.objects.create(user=user,
                       balance=0.0,
                       total=0.0)
print('admin数据导入完成')
