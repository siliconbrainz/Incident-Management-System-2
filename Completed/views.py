from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from twilio.rest import Client
from django.conf import settings
from CustomerData.models import CustomerTrack
from CustomerData.serializers import CustomerTrackSerializer


# Create your views here.
class DropCompletedView(APIView):
    def get(self, request, customerToken=None, format=None):
        if customerToken == None:
            customer = [(customer.rcNo,customer.customer_token) for customer in CustomerTrack.objects.all()]
            testdata = []
            for i in customer:
                Salesdata = [ testdata.append( CustomerTrackSerializer(SalesData))  for SalesData in CustomerTrack.objects.all().filter(
                    rcNo__iexact=i[0],customer_token=i[1], status__iexact='COMPLETED')]
                
            return Response({'Completed': testdata})
        else:
            try:
                customer = CustomerTrack.objects.get(customer_token=customerToken)
                CustomerData = [CustomerTrackSerializer(SalesData) for SalesData in CustomerTrack.objects.all().filter(
                    customer_token__iexact=customer.customer_token,status__iexact='COMPLETED')]
                return Response({'Completed': CustomerData})
            except:
                return Response({'Message': 'Requst NotFound'})
