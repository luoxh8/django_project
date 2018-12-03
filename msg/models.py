from django.db import models
from markdownx.models import MarkdownxField

from core.models import CoreModel
from users.models import Profile


class Msg(CoreModel):
    MSG_TYPE = (
        (1, '竞拍消息'),
        (2, '拍卖公告'),
        (3, '系统消息'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    msg_type = models.IntegerField(choices=MSG_TYPE, verbose_name='消息类型')
    content = MarkdownxField()
    periods = models.IntegerField(verbose_name='公告期数')

    class Meta:
        verbose_name = '消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MsgHandler(CoreModel):
    sender = models.ForeignKey(Profile, models.DO_NOTHING,
                               null=True, blank=True,
                               related_name='sender',
                               verbose_name='发送人')
    receiver = models.ForeignKey(Profile, models.DO_NOTHING,
                                 null=True, blank=True,
                                 related_name='receiver',
                                 verbose_name='收件人')
    msg = models.ForeignKey(Msg, models.CASCADE, verbose_name='消息')

    class Meta:
        verbose_name = '消息处理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}--{}--{}'.format(self.sender.username, self.receiver.username, self.msg.title)
