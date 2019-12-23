from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import DevUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = DevUser
    list_display = ('email', 'is_staff', 'is_active','first_name','last_name','date_joined','last_login')
    list_filter = ('email', 'is_staff', 'is_active','first_name','last_name','date_joined','last_login')
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','date_joined','last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(DevUser, CustomUserAdmin)