from django.contrib.admin import ModelAdmin, register
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from goods.models import BidRecord, Category, Goods, GoodsImage, RoomDetail


@register(Goods)
class GoodsAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


@register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@register(GoodsImage)
class GoodsImageAdmin(ModelAdmin):
    pass


@register(BidRecord)
class BidRecordAdmin(ModelAdmin):
    pass


@register(RoomDetail)
class RoomDetailAdmin(ModelAdmin):
    pass
