from rest_framework.serializers import ModelSerializer
from .models import PickUp


class PickUpSerializer(ModelSerializer):
    class Meta:
        model = PickUp
        fields = '__all__'
