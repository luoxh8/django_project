import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()

from db_tool.data.category_data import category_data
from goods.models import Category

for data in category_data:
    category = Category()
    category.name = data['name']
    category.image = data['image']
    category.index = data['index']
    category.save()

print('category数据导入完成')
