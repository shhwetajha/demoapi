from django.contrib.auth.backends import ModelBackend
from  accounts.models import Users



class EmailBackends(object):
    def authenticate(self,request,username=None,password=None,**kwargs):
        try:
           user= Users.objects.get(Email_Address=username)    
        except Users.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            return None
