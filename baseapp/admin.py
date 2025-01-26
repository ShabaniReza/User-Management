from django.contrib import admin
from .models import Profile, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']
    list_editable = ['role']
    list_per_page = 10
    search_fields = ['username__istartswith', 'email__istartswith', 'role__istartswith']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number', 'address']
    search_fields = ['phone_number__istartswith', 'address__istartswith']
    list_per_page = 10