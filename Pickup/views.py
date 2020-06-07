from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import PickUpSerializer

from django.conf import settings
from twilio.rest import Client

from CustomerData.models import SalesData, CSR
from CustomerData.serializers import CSRSerializer, SalesDataSerializer
from .serializers import PickUpSerializer


class PickupView(APIView):
    def get(self, request, rcNo=None, format=None):
        if rcNo == None:
            rcNo = [rcNo.rcNo for rcNo in CSR.objects.all()]
            testdata = []
            for i in rcNo:
                Salesdata = [{"name": SalesData.name, "address": SalesData.address, "phNo": SalesData.phNo, "email": SalesData.email, "address": SalesData.email, "rcNo": SalesData.rcNo, "version": SalesData.version, "data_of_purchased": SalesData.purchase_date} for SalesData in SalesData.objects.all().filter(
                    rcNo__iexact=i)]
                testdata.append(Salesdata)
            return Response({'Assigned': testdata})
        else:
            rcNo = CSR.objects.get(rcNo=rcNo)
            Salesdata = [{"name": SalesData.name, "address": SalesData.address, "phNo": SalesData.phNo, "email": SalesData.email, "address": SalesData.email, "rcNo": SalesData.rcNo, "version": SalesData.version, "data_of_purchased": SalesData.purchase_date} for SalesData in SalesData.objects.all().filter(
                rcNo__iexact=rcNo.rcNo)]
            return Response({'Assigned': Salesdata})

    def post(self, request, rcNo=None, format=None):
        data = request.data
        SalesData1 = SalesData.objects.get(rcNo=rcNo)
        # Salesdata = {"name": SalesData1.name, "address": SalesData1.address, "phNo": SalesData1.phNo, "email": SalesData1.email,
        #              "address": SalesData1.email, "rcNo": SalesData1.rcNo, "version": SalesData1.version, "data_of_purchased": SalesData1.purchase_date}
        serializer = PickUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save(rcNo=rcNo,user=request.user)
            # client = Client(settings.TWILIO_ACCOUNT_SID,
            #                 settings.TWILIO_AUTH_TOKEN)

            # message = 'Hi '+SalesData1.name + \
            #     ' your vehicle ' + SalesData1.rcNo + ' has been picked by the driver ' + \
            #     request.user.first_name + ' ' + request.user.last_name + ' +919008088227'
            # client.messages.create(
            #     to=settings.CUSTOMER_NUMBER,
            #     from_=settings.TWILIO_NUMBER,
            #     body=message + u'\U0001f680')
            return Response({'data': serializer.data})
        else:
            return Response({'data': 'Please upload the valid information'})

