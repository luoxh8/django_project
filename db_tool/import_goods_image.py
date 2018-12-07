import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django

django.setup()

from db_tool.data.goods_image_data import goods_image_data
from goods.models import Goods, GoodsImage

count = [0, 1, 2, 3, 4]

goods_list = Goods.objects.all()
for goods in goods_list:
    for i in count:
        GoodsImage.objects.create(
            index=goods_image_data['index'],
            image=goods_image_data['image'],
            goods=goods,
        )

print('goods_image导入成功')
