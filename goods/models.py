from django.db import models
from markdownx.models import MarkdownxField

from core.models import CoreModel
from users.models import Profile


class Category(CoreModel):
    name = models.CharField(max_length=15, blank=True, null=True, verbose_name='类型名称')
    image = models.ImageField(upload_to='category/image/', verbose_name='类型的图片')
    index = models.IntegerField(verbose_name='排序')

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(CoreModel):
    goods_id = models.CharField(max_length=64, unique=True, db_index=True, verbose_name='商品id')
    category = models.ForeignKey(Category, models.DO_NOTHING, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, blank=True, null=True, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    market_price = models.FloatField(default=0.00, verbose_name="市场价格")
    now_price = models.FloatField(default=0.00, verbose_name="现在价格")
    step_price = models.FloatField(default=1, verbose_name='每次出价价格')
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_desc = MarkdownxField(verbose_name='商品描述')
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/front/image", verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热拍")
    is_sell = models.BooleanField(default=False, verbose_name="是否拍出")
    periods = models.IntegerField(verbose_name='期数')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(CoreModel):
    """
        商品轮播图
    """
    index = models.IntegerField(default=0, verbose_name='图片顺序')
    goods = models.ForeignKey(Goods, models.DO_NOTHING, verbose_name="商品")
    image = models.ImageField(upload_to="goods/detail/image", verbose_name="图片")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class RoomDetail(CoreModel):
    name = models.CharField(max_length=100, verbose_name='房间名字')
    goods = models.ForeignKey(Goods, models.CASCADE, verbose_name='商品')
    onlookers = models.IntegerField(verbose_name='围观人数')
    bidders = models.IntegerField(verbose_name='出价人数')

    class Meta:
        verbose_name = '房间详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BidRecord(CoreModel):
    goods = models.ForeignKey(Goods, models.DO_NOTHING, verbose_name='商品')
    profile = models.ForeignKey(Profile, models.DO_NOTHING, verbose_name='出价人')
    is_out = models.BooleanField(default=True, verbose_name='是否出局')

    class Meta:
        verbose_name = '出价记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}---{}'.format(self.goods.name, self.profile.username)
