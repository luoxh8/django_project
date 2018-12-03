from django.db import models

from core.models import CoreModel
from goods.models import Category, Goods


class Banner(CoreModel):
    """
        轮播的商品
    """
    goods_id = models.CharField(max_length=64, null=True, blank=True, default='', verbose_name='商品ID')
    title = models.CharField(max_length=20, verbose_name='标题')
    image = models.ImageField(upload_to='homes/banner/image', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    url = models.CharField(max_length=512, null=True, blank=True, verbose_name='url')
    activity = models.CharField(max_length=30, null=True, blank=True, verbose_name="跳转控制器")

    class Meta:
        verbose_name = '首页Banner'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Topic(CoreModel):
    """
        首页banner图下面的主题
    """
    category_id = models.IntegerField(null=True, blank=True, default=0, verbose_name='类型ID')
    title = models.CharField(max_length=20, verbose_name='标题')
    icon = models.ImageField(upload_to='homes/topic/icon', verbose_name="图标")
    index = models.IntegerField(default=0, verbose_name="排列顺序")
    url = models.CharField(max_length=512, null=True, blank=True, verbose_name='url')
    activity = models.CharField(max_length=30, null=True, blank=True, verbose_name="跳转控制器")

    class Meta:
        verbose_name = '首页Topic'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
