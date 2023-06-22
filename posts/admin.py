from django.contrib import admin
from .models import Post, PostFile



class PostFileInlineAdmin(admin.TabularInline):
    model = PostFile
    field = ('file', )
    extra = 0
    can_delete = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_time')
    inlines = (PostFileInlineAdmin,)
    # actions = None

    # def has_delete_permission(self, request, obj = None):
    #     return False

    # def has_add_permission(self, request, obj = None):
    #     return False
# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):

    