import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()

from db_tool.data.goods_data import goods_data
from goods.models import Category, Goods

for data in goods_data:
    goods = Goods()
    goods.goods_id = data['goods_id']
    goods.category = Category.objects.filter(pk=data['category']).first()
    goods.name = data['name']
    goods.market_price = data['market_price']
    goods.goods_brief = data['goods_brief']
    goods.goods_desc = data['goods_desc']
    goods.goods_front_image = data['goods_front_image']
    goods.periods = data['periods']
    goods.save()

print('goods数据导入完成')
