from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# now useradmin will known as BaseUserAdmin
from account.models import User


# Register your models here.

class UserModelAdmin(BaseUserAdmin):
   
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email","name","tc","is_admin"]
    list_filter = ["is_admin"]  #kiske base par humara list filter hai wo yaha mention hai
    fieldsets = [
        ('User Credentialis', {"fields": ["email", "password"]}),#User credentials  as a title show hoga ab next fieldset 
        ("Personal info", {"fields": ["name","tc"]}),             #jo user credentials ke liye jana jayega
        # ese hi personalinfo me name and tc de denge
        ("Permissions", {"fields": ["is_admin"]}),
        #permissions ek section banega jisme isadmin hume dikhayi dega
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],#agar css apply karna chhte hai to yaha class de sakte hai
                "fields": ["email","name","tc","password1", "password2"],
    # yaha par ese fields ko likhte hai jo hum chahte hai display ho create object page par
            },
        ),
    ]
    search_fields = ["email"] #email ke base par search karna chahte hai
    ordering = ["email","id"] #email and id ke base par ordering karna chahte hai isliye
    filter_horizontal = [] #kis tareeke se filter karna chahenge horizontal wo likha hua hai


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
# User jo model hai and useradmin jo humne abhi create kia hai
# User model ke liye humne usermodelAdmin ko register kia hua hai
