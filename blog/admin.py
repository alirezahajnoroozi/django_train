from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["title", "status", "counted_views", "published_date"]
    empty_value_display = "-empty-"

admin.site.register(Post, PostAdmin)