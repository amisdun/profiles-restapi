from rest_framework import serializers

class HellSerializer(serializers.Serializer):
    """A name feld for testing our APIview"""
    name = serializers.CharField(max_length=10)
