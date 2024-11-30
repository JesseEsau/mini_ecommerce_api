from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'city', 'state', 'address', 'phone']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('city', 'state', 'address', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('city', 'state', 'address', 'phone')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
