from rest_framework.serializers import ModelSerializer
from .models import CSR, SalesData


class CSRSerializer(ModelSerializer):
    class Meta:
        model = CSR
        fields = '__all__'


class SalesDataSerializer(ModelSerializer):
    class Meta:
        model = SalesData
        fields = '__all__'
