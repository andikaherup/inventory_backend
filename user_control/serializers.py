from rest_framework import serializers
from .models import CustomUser

class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    fullname = serializers.CharField()
    role = serializers.ChoiceField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EnailField()
    password = serializers.CharField(required=false)
    is_new_user = serializers.BooleanField(default=false, required=false)