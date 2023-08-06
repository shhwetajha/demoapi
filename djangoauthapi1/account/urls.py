from django.urls import path
from account.views import UserRegisterationView

#url=api/user/
urlpatterns=[
    path('register/',UserRegisterationView.as_view(),name='UserRegisterationView')

]