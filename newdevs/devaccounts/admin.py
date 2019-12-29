from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .forms import CustomEmployerChangeForm, CustomEmployerCreationForm

from .models import DevUser, EmployerAccount


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

class CustomEmployerAccountAdmin(UserAdmin):
    add_form = CustomEmployerCreationForm
    form = CustomEmployerChangeForm
    model = EmployerAccount
    list_display = ('email', 'is_staff', 'is_active','first_name','last_name','date_joined','last_login','company_name')
    list_filter = ('email', 'is_staff', 'is_active','first_name','last_name','date_joined','last_login','company_name')
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','date_joined','last_login','company_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','company_name')
    ordering = ('email','company_name')


admin.site.register(EmployerAccount, CustomEmployerAccountAdmin)