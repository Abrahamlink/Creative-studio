from django.contrib import admin
from .models import NewsPost, ImagePost, Comment, Tag, ActionType


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type_name', 'pubdate', 'studio_name', 'id')
    list_filter = ('studio_name',)


class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'video')
    list_filter = ['product']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'author_email', 'site', 'pubdate')


admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(ImagePost, ImagePostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(ActionType)
