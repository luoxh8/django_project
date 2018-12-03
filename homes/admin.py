from django.contrib.admin import ModelAdmin, register

from homes.models import Banner, Topic


@register(Banner)
class BannerAdmin(ModelAdmin):
    pass


@register(Topic)
class TopicAdmin(ModelAdmin):
    pass
