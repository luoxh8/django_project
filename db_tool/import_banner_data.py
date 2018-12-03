import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()

from db_tool.data.banner_data import banner_data
from homes.models import Banner

for banner in banner_data:
    Banner.objects.create(title=banner['title'],
                          image=banner['image'],
                          index=banner['index'])
print('banner数据导入完成')
