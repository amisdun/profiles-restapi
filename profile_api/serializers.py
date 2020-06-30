from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """A name feld for testing our APIview"""
    name = serializers.CharField(max_length=10)
