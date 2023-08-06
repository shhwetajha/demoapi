from django.urls import path

# http://127.0.0.1:8000/


from .views import *
from accounts.main import *


urlpatterns = [
  
    # path('login/',index,name='login'),
    # path('forgetPassword/',fpass,name='fpass'),
    path('registeration/', Register_Users,name='registeration'),
    path('login/',login_user,name='login'),
    path('forgot/',forgot_password,name='forgot_password'),
    # path('',forgott,name='forgot'),
    path('success/',success,name='success'),
    path('logout/',view_logout,name='logout'),
    path('reset/',view_reset_password,name='reset'),
    path('twilio/',sendsms,name='twilio'),
    path('for/',view_templatepassword,name='for')
    


]