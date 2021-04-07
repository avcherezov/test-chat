from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("pk", 'sender', 'recipient', 'message', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(Message, MessageAdmin)
