from django.contrib import admin
from .models import Kanji
# Register your models here.

class KanjiAdmin(admin.ModelAdmin):
    list_display = ('character', 'level', 'is_number', 'is_radical', 'meaning', 'example')
    list_filter = ('level', 'is_number', 'is_radical', )



admin.site.register(Kanji, KanjiAdmin)

