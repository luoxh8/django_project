import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()

from db_tool.data.msg_data import msg_data
from msg.models import Msg

for msg in msg_data:
    Msg.objects.create(
            title=msg['title'],
            content=msg['content'],
            periods=msg['periods'],
            msg_type=msg['msg_type'],
    )

print('msg数据导入完成')
