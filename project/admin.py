from django.contrib import admin
from .models import Proj

# Register your models here.
class ProjAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter  =['date']
    search_fields  =['body']
    
admin.site.register(Proj, ProjAdmin)