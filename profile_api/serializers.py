from rest_framework import serializers
from profile_api import models


class HelloSerializer(serializers.Serializer):
    """A name feld for testing our APIview"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(Serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'iput_type': 'password'}
            }
        }

    def create(self,validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
