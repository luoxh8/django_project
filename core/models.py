from django.db import models
from django.db.models import Manager


class CoreManager(Manager):

    def get_queryset(self):
        return super(CoreManager, self).get_queryset().filter(is_delete=False)


class CoreModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否被删除')
    objects = CoreManager()

    class Meta:
        abstract = True
