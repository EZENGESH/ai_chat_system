from rest_framework import serializers
from .models import User, Chat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value.lower()

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['message', 'response', 'timestamp']
