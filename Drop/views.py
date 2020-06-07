from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from twilio.rest import Client
from django.conf import settings
from CustomerData.models import CSR, SalesData
from .serializers import DropSerializer
from .models import Drop


class DropView(APIView):
    def get(self, request, rcNo=None, format=None):
        if rcNo != None:
            rcNo = CSR.objects.get(rcNo=rcNo)
            Salesdata = [{"name": SalesData.name, "address": SalesData.address, "phNo": SalesData.phNo, "email": SalesData.email, "address": SalesData.email, "rcNo": SalesData.rcNo, "version": SalesData.version, "data_of_purchased": SalesData.purchase_date} for SalesData in SalesData.objects.all().filter(
                rcNo__iexact=rcNo.rcNo)]
            return Response({'Assigned': Salesdata})
        else:
            return Response({'message': 'Request is not valid'})

    def post(self, request, rcNo=None, format=None):
        data = request.data
        serializer = DropSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            # client = Client(settings.TWILIO_ACCOUNT_SID,
            #                 settings.TWILIO_AUTH_TOKEN)

            # message = 'Your vehicle has been dropped thank you for reaching us fell free to provide feedback ' + \
            #     request.user.first_name + ' ' + request.user.last_name + ' +919008088227'
            # client.messages.create(
            #     to=settings.CUSTOMER_NUMBER,
            #     from_=settings.TWILIO_NUMBER,
            #     body=message + u'\U0001f680')
            return Response({'data': serializer.data})
        else:
            return Response({'data': 'Please upload the valid data'})
