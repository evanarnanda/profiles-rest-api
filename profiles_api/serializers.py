from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing RESTView"""
    name = serializers.CharField(max_length = 10)
