from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):
    model=Users
    fields=("Email_Address",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        models=Users
        fields=("Email_Address",)