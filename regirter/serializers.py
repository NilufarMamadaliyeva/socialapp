from django.contrib.auth.models import User
from rest_framework import serializers,validators
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that email already exists.")]
    )
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user