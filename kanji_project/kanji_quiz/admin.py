from django.contrib import admin
from .models import Kanji, Portuguese
# Register your models here.

class KanjiAdmin(admin.ModelAdmin):
    list_display = ('character', 'level', 'is_number', 'is_radical')
    list_filter = ('level', 'is_number', 'is_radical')

class PortugueseAdmin(admin.ModelAdmin):
    list_display = ('meaning', 'example')

admin.site.register(Kanji, KanjiAdmin)
admin.site.register(Portuguese, PortugueseAdmin)
