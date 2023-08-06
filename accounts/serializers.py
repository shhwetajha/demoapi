from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import *

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = Users
            fields = "__all__"

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    # password2=serializers.CharField(style={"input-type":"password"},write_only=True)
    class Meta:
        model = Users
        fields = ('username', 'Email_Address', 'zipcode', 'Date_of_Birth','password', 'Mobileno')
        

    def create(self, Validated_data):
        return Users.objects.create(**Validated_data)

        # return user
    
class EmailSerializer(serializers.Serializer):
    email=serializers.EmailField()


    class Meta:
        fields=("email",)
    


    