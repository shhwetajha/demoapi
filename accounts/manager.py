from django.contrib.auth.base_user import BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, Email_Address, username=None, birthday=None, zipcode=None,password=None):
        if not Email_Address:
            raise ValueError('Users must have an email address')

        user = self.model(
            Email_Address=self.normalize_email(Email_Address),
            Date_of_Birth=birthday,
            zipcode=zipcode,Username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,Email_Address,password):
        user = self.create_user(Email_Address=self.normalize_email(Email_Address),password=password,username=username)
        user.is_admin = True
        user.is_active=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)