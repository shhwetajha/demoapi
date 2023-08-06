from django.shortcuts import render
from rest_framework import APIView
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import apiview


# Create your views here.
