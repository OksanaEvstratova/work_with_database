from django.contrib import admin

# Register your models here.
from phones.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'release_date', 'lte_exists', 'slug']
    list_filter = ['name', 'lte_exists']