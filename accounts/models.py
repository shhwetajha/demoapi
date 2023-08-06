from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import MyAccountManager
from django.contrib.auth.models import User

# Create your models here.


class Users(AbstractBaseUser,PermissionsMixin):
    Email_Address = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    Date_of_Birth = models.CharField(max_length=30, blank=True, null=True, default=None)
    name = models.CharField(max_length=30, blank=True, null=True)
    username= models.CharField(max_length=30,unique=True, blank=True, null=True)
    Mobileno= models.CharField(max_length=19,unique=True, blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super_teacher = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    # 'Email_Address'

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.Email_Address)


    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser
