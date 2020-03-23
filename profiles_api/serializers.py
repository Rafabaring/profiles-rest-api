from rest_framework import serializers

# Aparentemente é uma class serializer por uma classe em views.py
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIview"""
    name = serializers.CharField(max_length = 10)
    x = serializers.IntegerField(max_value = None)
    y = serializers.IntegerField(max_value = None)
