from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from twilio.rest import Client
from django.conf import settings
from CustomerData.models import CSR, SalesData,CustomerTrack
from .serializers import DropSerializer
from CustomerData.serializers import CSRSerializer, SalesDataSerializer,CustomerTrackSerializer
from .models import Drop


class DropView(APIView):
    def get(self, request, customerToken=None, format=None):
        if customerToken == None:
            customer = [(customer.rcNo,customer.customer_token) for customer in CustomerTrack.objects.all()]
            testdata = []
            for i in customer:
                Salesdata = [ testdata.append( CustomerTrackSerializer(SalesData))  for SalesData in CustomerTrack.objects.all().filter(
                    rcNo__iexact=i[0],customer_token=i[1], status__iexact='PICKED')]
                
            return Response({'Picked': testdata})
        else:
            try:
                customer = CustomerTrack.objects.get(customer_token=customerToken)
                Salesdata = [CustomerTrackSerializer(SalesData) for SalesData in CustomerTrack.objects.all().filter(
                    customer_token__iexact=customer.customer_token,status__iexact='PICKED')]
                return Response({'Picked': Salesdata})
            except:
                return Response({'Message': 'Requst NotFound'})

    def post(self, request, customerToken=None, format=None):
        data = request.data
        SalesData1= CustomerTrack.objects.get(
                customer_token=customerToken)
        if SalesData1.status=='COMPLETED':
            return(Response({'Message':'Request is completd'}))
        elif SalesData1.status=='PICKED':
            serializer = DropSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                SalesData1.status='COMPLETED'
                SalesData1.save()
                CustomerData = [CustomerTrackSerializer(SalesData) for SalesData in CustomerTrack.objects.all().filter(
                    customer_token=customerToken,status__iexact='COMPLETED')]
                # client = Client(settings.TWILIO_ACCOUNT_SID,
                #                 settings.TWILIO_AUTH_TOKEN)

                # message = 'Your vehicle has been dropped thank you for reaching us fell free to provide feedback ' + \
                #     request.user.first_name + ' ' + request.user.last_name + ' +919008088227'
                # client.messages.create(
                #     to=settings.CUSTOMER_NUMBER,
                #     from_=settings.TWILIO_NUMBER,
                #     body=message + u'\U0001f680')
                return Response({'CompletedDetails': serializer.data,
                                'CustomerData':CustomerData})
            else:
                return Response({'Message': 'Please upload the valid data'})


