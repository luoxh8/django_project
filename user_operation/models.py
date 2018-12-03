from django.db import models

from core.models import CoreModel
from goods.models import Goods
from users.models import Profile


class Collection(CoreModel):
    goods = models.ForeignKey(Goods, models.CASCADE, verbose_name='商品')
    user = models.ForeignKey(Profile, models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}--{}'.format(self.user.username, self.goods.name)


class Code(CoreModel):
    ACTION = (
        (1, '注册'),
        (2, '重置密码'),
        (3, '提现'),
    )
    code = models.CharField(max_length=8, verbose_name='验证码')
    action = models.IntegerField(choices=ACTION, verbose_name='动作')
    user = models.ForeignKey(Profile, models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}--{}'.format(self.user.username, self.created_time)
