from django.contrib import admin

from .models import Category,Quiz
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category')
    list_display_links=('id','category')

class QuizAdmin(admin.ModelAdmin):
    list_display=('id','quiz')
    list_display_links=('id','quiz')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Quiz,QuizAdmin)