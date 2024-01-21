from django.contrib import admin

from .models import Diary,DiaryGood
class DiaryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class DiaryGoodAdmin(admin.ModelAdmin):
    list_display=('id','good_user')
    list_display_links=('id','good_user')

admin.site.register(Diary,DiaryAdmin)
admin.site.register(DiaryGood,DiaryGoodAdmin)