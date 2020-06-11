from rest_framework.serializers import ModelSerializer
from .models import Drop


class DropSerializer(ModelSerializer):
    class Meta:
        model = Drop
        fields = '__all__'
    