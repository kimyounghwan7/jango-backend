# users serializers

from rest_framework import serializers
from .models import User, UserImage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
        
class UserUploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = [
            'user',
            'image_url'
        ]

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = [
            'user',
            'image_url',
            'image_reg_date'
        ]
        