from  rest_framework import  serializers

class Serializer(serializers.Serializer):
    """serializando nombre"""
    name=serializers.CharField(max_length=10)