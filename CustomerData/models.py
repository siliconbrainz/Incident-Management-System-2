from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4

class SalesData(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phNo = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(
        max_length=255, null=True, blank=True, unique=True)
    rcNo = models.CharField(max_length=255, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=255, null=True, blank=True)


class CSR(models.Model):
    rcNo = models.CharField(max_length=255, null=True, blank=True)

    @property
    def get_rcNo(self):
        return self.rcNo

    def __str__(self):
        return str(self.rcNo)

class CustomerTrack(models.Model):
    STATUS=(('ASSIGNED','ASSIGNED'),('PENDING','PENDING'),('COMPLETED','COMPLETED'))
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phNo = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(
        max_length=255, null=True, blank=True)
    rcNo = models.CharField(max_length=255, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    status=models.TextField(max_length=255, null=True, blank=True,choices=STATUS,default='ASSIGNED')
    customer_token=models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)



@receiver(post_save, sender=CSR)
def TransferSalesDataToCustomerData(sender, instance, **kwargs):
    try:
        customer = CustomerTrack.objects.get(rcNo=instance.rcNo)
        if customer.status =='COMPLETED':
            [CustomerTrack.objects.create(name=data.name,address=data.address,phNo=data.phNo,email=data.email,rcNo=data.rcNo,purchase_date=data.purchase_date, model=data.model,status='ASSIGNED',customer_token=uuid4()) for data in SalesData.objects.all().filter( rcNo__iexact=instance.rcNo)]
    except  :
        [CustomerTrack.objects.create(name=data.name,address=data.address,phNo=data.phNo,email=data.email,rcNo=data.rcNo,purchase_date=data.purchase_date, model=data.model,status='ASSIGNED',customer_token=uuid4()) for data in SalesData.objects.all().filter( rcNo__iexact=instance.rcNo)]

    