from django.contrib import admin

from .models import Category,ChickPost,Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class ChickPostAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class CommentAdmin(admin.ModelAdmin):
    list_display=('id','thoughts_on_comment')
    list_display_links=('id','thoughts_on_comment')

admin.site.register(Category,CategoryAdmin)
admin.site.register(ChickPost,ChickPostAdmin)
admin.site.register(Comment,CommentAdmin)