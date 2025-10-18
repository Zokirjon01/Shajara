from django.contrib import admin
from .models import Odam

# Register your models here.

@admin.register(Odam)
class OdamAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'yosh', 'father', 'mother')
    search_fields = ('full_name',)