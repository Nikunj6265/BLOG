from django.contrib import admin
from .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','timestamp','author']


