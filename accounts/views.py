from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import login,logout
from rest_framework import permissions,status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
# from django_token.models import Token
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate
from django.forms import ValidationError
from .models import Users
from demoapi import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
# Create your views here.

# Register API

    



def index(request) :
    return render(request,'login.html') 

def fpass(request):
    return render(request,'forgetpassword.html')

@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request):
    password=request.data['password']
    serializer= RegisterSerializer(data=request.data)
    if serializer.is_valid():
        account=serializer.save()
        account.set_password(password)
        account.save()
        Token.objects.create(user=account)
        return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
    else:
        return Response({'errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    reqbody=request.data
    username=reqbody['username']
    password=reqbody['password']
    auth=authenticate(request,username=username,password=password)
    if auth:
            if Token.objects.filter(user=auth).exists():
                token=Token.objects.get(user=auth)
                token.delete()
                token=Token.objects.create(user=auth)
                login(request,auth)
            # print(token)
                return Response({"message":"success","token":token.key})
            else:
                login(request,auth)
                token=Token.objects.create(user=auth)
                return Response({"message":"success","token":auth.Email_Address})
    else:
            raise ValidationError({"400":f"Account doesnot exist"})
    
        
"""@permission_classes([AllowAny])
@api_view(['POST'])
def view_login(request):
    reqbody=request.data
    email=reqbody['Email_Address']
    password=reqbody['password']
    auth=authenticate(request,username=email,password=password)
    if auth:
        if Token.objects.filter(user=auth).exists():
            token=Token.objects.get(user=auth)
            token.delete()
            token=Token.objects.create(user=auth)
            login(request,auth)
            return Response({"message":"success","token":token.key})
        else:
            token=Token.objects.create(user=auth)
            login(request,auth)
            return Response({"message":"success","token":auth.Email_Address}) 
    else:
        raise ValidationError({"400":f"Account doesnot exist"})   


def login_user(request):
    reqbody=request.data
    email=reqbody['Email_Address']
    password=reqbody['password']
    auth=authenticate(request,username=email,password=password)
    if auth:
        if Token.objects.filter(user=auth).exists():
            token=Token.objects.get(user=auth)
            token.delete()
            token=Token.objects.create(user=auth)
            login(request,auth)
            # print(token)
            return Response({"message":"success","token":token.key})
        else:
            login(request,auth)
            token=Token.objects.create(user=auth)
            return Response({"message":"success","token":auth.Email_Address})
    else:
        raise ValidationError({"400":f"Account doesnot exist"})"""
   





@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    Email_Address=request.data.get("Email_Address")
    New_Password=request.data.get("New_Password")
    confirm_password=request.data.get("confirm_password")


    user=Users.objects.filter(Email_Address=Email_Address)
    if user.exists():
        user=Users.objects.get(Email_Address=Email_Address)
        if New_Password==confirm_password:
            user.set_password(confirm_password)
            user.save()
            subject="Congratulations!"+" "+str(user.name)+" "+"Pin reset successfully!!!"
            email_from=settings.EMAIL_HOST_USER
            message="Project:"+str(user.Email_Address)+"\nPin :"+New_Password
            recipient_list=["sjha123321@gmail.com"]
            send_mail(subject,message,email_from,recipient_list)
            return Response({"error":False,"message":"Password resetted successfully"})
        else:
            return Response({"error":True,"message":"Password and confirm password do not match"})
    else:
        return Response({"error":False,"message":"User doesnot exist"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def forgot_password(request):
    if request.method=='POST':
        Email_Address=request.POST("Email_Address")
        New_Password=request.POST("New_Password")
        confirm_password=request.POST("confirm_password")
        username=request.POST("username")


        if Users.objects.filter(Email_Address=Email_Address).exists():
            if New_Password==confirm_password:
                Users.set_password(confirm_password)
                mydict={'username':username}
                Users.save()
                html_template='register_email.html'
                html_message=render_to_string(html_template,context=mydict)
                subject='WELCOME TO SERVICE-VICE-VERSA'
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[Email_Address]
                message=EmailMessage(subject, html_message, email_from, recipient_list)
                message.content_subtype='html'
                message.send()
                return redirect("success")
                # messages.info(request,'Password changed')
                # return redirect ("register")
            else:
                return Response({"error":True,"message":"Password and confirm password do not match"})
        else:
            return Response({"error":False,"message":"User doesnot exist"})
    else:
        return render(request,'register.html')
    
def success(request):
    return render(request,'success.html')


@permission_classes([AllowAny])
@api_view(['POST'])
def view_registeration(request):
    password=request.data['password']
    serial=RegisterSerializer(data=request.data)
    if serial.is_valid():
        account=serial.save()
        account.set_password=password
        account.save()
        Token.objects.create(user=account)
        return Response({"data":serial.data},status=status.HTTP_201_CREATED)
    else:
        return Response({"errors":serial.errors},status=status.HTTP_403_FORBIDDEN)
    


@api_view(['GET'])
@permission_classes([AllowAny])
def view_logout(request):
    Token.objects.get(user=request.user).delete()
    logout(request)
    return Response({"message":"User logged Out successfully!!!"})
    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def view_reset_password(request):
    user=request.user.id
    old_password=request.data.get('old_password')
    password=request.data.get('password')
    new_password=request.data.get('new_password')
    user=Users.objects.get(id=user)
    if old_password:
        if (user.check_password(old_password)):
            if password==new_password:
                user.set_password(new_password)
                user.save()
                subject="Congaratulations"+str(user.Email_Address)+"Your password reset successfully!!!"
                email_from=settings.EMAIL_HOST_USER
                message="project"+str(user.Email_Address)+"pin"+user.password
                recipient_list=[user.Email_Address]
                msg=EmailMultiAlternatives(subject,message,email_from,recipient_list)
                msg.attach_file("C:/Users/dell/OneDrive/Desktop/dummy.pdf")
                send=msg.send(fail_silently=False)
                #print(send)
                #print("send",send)
                # send_mail(subject,message,email_from,recipient_list)
                return Response({'error':False,'message':'password reset successfully!!!'})
            else:
                return Response({'error':True,'message':'password and confirm_password do not match'})
        else:
            return Response({'error':True,'message':'old password is not correct'})
    else:
        return Response({'error':True,'message':'old password cannot be blank'})
    


@api_view(['POST'])
@permission_classes([AllowAny])
def view_templatepassword(request):
    Email_Address=request.data.get('Email_Address')
    new_password=request.data.get('new_password')
    confirm_password=request.data.get('confirm_password')
    username=request.data.get('username')
    users=Users.objects.filter(Email_Address=Email_Address)
    if users.exists():
            users=Users.objects.get(Email_Address=Email_Address)
            print(users)
            if new_password==confirm_password:
                users.set_password(new_password)
                mydict={'username':username}
                users.save()
                html_template='firstfile.html'
                html_message=render_to_string(html_template,context=mydict)
                subject='Congrats! Your Password has been changed'
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[users.Email_Address]
                # msg='Your password just got changed'
                message=EmailMessage(html_message,subject,email_from,recipient_list)
                message.content_subtype='html'
                message.send()
        
                # msg=EmailMultiAlternatives(subject,message,email_from,recipient_list)
                # msg.attach_file('C:/Users/dell/OneDrive/Desktop/dummy.pdf')
                # send=msg.send(fail_silently=False)
                return Response({'error':False,'message':'Password changed'})
            else:
                return Response({'error':True,'message':'Password and confirm_password do not match'})
    else:
        return Response({'error':True,'message':'Account doesnot exist'})


   # {"Email_Address":"sjha123321@gmail.com",
#"new_password":"1234",
#"confirm_password":"1234"}