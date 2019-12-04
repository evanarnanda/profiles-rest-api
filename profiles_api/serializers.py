from rest_framework import serializers


from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing RESTView"""
    name = serializers.CharField(max_length = 10)


class UserProfileSerilizer(serializers.ModelSerializer):
    """Form profile for testing RESTView"""

    class Meta:
        model = models.UserProfiles
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return new user"""
        user = models.UserProfiles.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
