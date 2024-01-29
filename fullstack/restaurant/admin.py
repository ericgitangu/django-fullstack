from django.contrib import admin 
from . import models

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'reservation_date', 'reservation_slot']
    search_fields = ['first_name']
    list_filter = ['reservation_date']

@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'menu_item_description']
    search_fields = ['name']
    list_filter = ['price']


