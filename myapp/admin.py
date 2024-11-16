from django.contrib import admin
from .models import *

@admin.register(MyUser)
class AdminMyUser(admin.ModelAdmin):
    list_display = ['email', 'date_of_birth', 'is_active']
    list_per_page = 10

@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    list_display = ['name', 'url']
    list_per_page = 10