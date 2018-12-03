import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()

from db_tool.data.topic_data import topic_data
from homes.models import Topic

for topic in topic_data:
    Topic.objects.create(
            title=topic['title'],
            icon=topic['icon'],
            index=topic['index'],
            url=topic['url']
    )
print('topic数据导入完成')
