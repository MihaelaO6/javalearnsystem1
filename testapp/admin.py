from django.contrib import admin
from .models import Post
# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("title","author",)
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Post, AdminPost)