from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import  User
from accounts.forms import CustomUserCreationForm
from accounts.forms import Users,CustomUserChangeForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=Users
    list_display=("Email_Address","is_staff","is_active")
    list_filter=("Email_Address","is_staff","is_active")
    fieldsets=(
        (None,{'fields':('Email_Address','password')}),(
        'Permissions',{'fields':('is_staff','is_active')}),
          )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('Email_Address','password1','password2','is_staff','is_active')}
            ),
    )


admin.site.register(Users,CustomUserAdmin)