from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter  =['date']
    search_fields  =['body']
    
admin.site.register(Post, PostAdmin)