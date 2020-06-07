from django.db import models


class SalesData(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phNo = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(
        max_length=255, null=True, blank=True, unique=True)
    rcNo = models.CharField(max_length=255, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=255, null=True, blank=True)


class CSR(models.Model):
    rcNo = models.CharField(max_length=255, null=True, blank=True)

    @property
    def get_rcNo(self):
        return self.rcNo

    def __str__(self):
        return str(self.rcNo)
