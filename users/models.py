from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import CoreModel


class Profile(AbstractUser):
    LEVEL = ((0, '普通用户'),
             (1, '一级用户'))

    PLATFORM = (('ios', '苹果用户'),
                ('android', '安卓设备'),
                ('core', '未知设备'))

    OAUTH_FORM = (('weixin', '微信'),
                  ('weibo', '微博'),
                  ('qq', 'QQ'),
                  ('phone', '手机'))

    GENDER = ((0, "女"),
              (1, "男"))

    uid = models.CharField(max_length=7, blank=True, null=True,
                           unique=True, db_index=True, verbose_name='uid')
    nick = models.CharField(max_length=30, null=True, blank=True,
                            default='', help_text='昵称', verbose_name='昵称')
    birthday = models.DateField(
        null=True, blank=True, help_text='出生年月', verbose_name="出生年月")
    gender = models.IntegerField(choices=GENDER, default=0, verbose_name="性别")
    platform = models.CharField(
        max_length=20, choices=PLATFORM, default='core', verbose_name='登录设备类型')
    device_id = models.CharField(
        max_length=40, null=True, blank=True, default='', verbose_name='设备id')
    register_ip = models.CharField(
        max_length=20, null=True, blank=True, default='', verbose_name='注册时候的IP')
    phone = models.CharField(max_length=11, default='',
                             null=True, blank=True, verbose_name='手机号码')
    level = models.CharField(max_length=2, choices=LEVEL,
                             default=0, verbose_name='用户等级')
    avatar = models.ImageField(
        upload_to='users/profile/avatar', null=True, blank=True, verbose_name='用户头像')

    # 第三方登录字段
    is_third = models.BooleanField(
        default=False, null=True, blank=True, verbose_name='是否都第三方登录')
    oauth_openid = models.CharField(
        max_length=128, default='', verbose_name='第三方openid')
    oauth_avatar = models.CharField(
        max_length=200, default='', verbose_name='第三方头像')
    oauth_from = models.CharField(
        choices=OAUTH_FORM, max_length=10, default='', verbose_name='验证来源')
    oauth_userinfo = models.TextField(
        default='', verbose_name='来自第三方平台的用户额外信息')
    oauth_time = models.DateTimeField(
        null=True, blank=True, verbose_name='绑定第三方帐号时间')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Balance(CoreModel):
    user = models.OneToOneField(Profile, models.CASCADE, verbose_name='用户')
    balance = models.FloatField(default=0.00, verbose_name='当前余额')
    total = models.FloatField(default=0.00, verbose_name='总充值')

    class Meta:
        verbose_name = "用户余额"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class PayAction(CoreModel):
    ACTION = ((1, '充值'),
              (2, '出价'),
              (3, '提现'))

    balance = models.ForeignKey(Balance, models.CASCADE, verbose_name='用于余额')
    action = models.IntegerField(choices=ACTION, verbose_name='操作')
    amount = models.IntegerField(verbose_name='具体金额')

    class Meta:
        verbose_name = "用户支付操作"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{action}--{name}--{amount}'.format(action=self.action, name=self.balance.user.username,
                                                   amount=self.amount)
