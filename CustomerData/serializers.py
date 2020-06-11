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

def CustomerTrackSerializer(SalesData):

    return {"name": SalesData.name, "address": SalesData.address, "phNo": SalesData.phNo, "email": SalesData.email, "address": SalesData.email, "rcNo": SalesData.rcNo, "model": SalesData.model,"customer_token":SalesData.customer_token, "data_of_purchased": SalesData.purchase_date}
