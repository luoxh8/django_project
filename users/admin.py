from django.contrib.admin import ModelAdmin, register

from users.models import Balance, PayAction, Profile


@register(Profile)
class ProfileAdmin(ModelAdmin):
    pass


@register(Balance)
class BalanceAdmin(ModelAdmin):
    pass


@register(PayAction)
class PayActionAdmin(ModelAdmin):
    pass
