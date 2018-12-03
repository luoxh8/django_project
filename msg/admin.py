from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from msg.models import Msg, MsgHandler


@admin.register(Msg)
class MsgAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


@admin.register(MsgHandler)
class MsgHandler(admin.ModelAdmin):
    pass
