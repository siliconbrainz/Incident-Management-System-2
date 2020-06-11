from django.db import models
from django.contrib.auth.models import User
from CustomerData.models import CSR


class PickUp(models.Model):
    FUEL_CHOOSE = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    )

    OdoMeter = models.DecimalField(
        max_digits=5, decimal_places=0, null=True, blank=True)
    FuelLevel = models.CharField(
        max_length=7, default=('1', '1'), choices=FUEL_CHOOSE, null=True, blank=True)
    CDPlayer = models.BooleanField(default=False)
    CigeretteCharger = models.BooleanField(default=False)
    ToolKit = models.BooleanField(default=False)
    ServiceBook = models.BooleanField(default=False)
    Clock = models.BooleanField(default=False)
    CarPerfume = models.BooleanField(default=False)
    Jack = models.BooleanField(default=False)
    SpareWheel = models.BooleanField(default=False)
    Mats = models.BooleanField(default=False)
    DickyMat = models.BooleanField(default=False)
    BodyCover = models.BooleanField(default=False)
    Antenna = models.BooleanField(default=False)
    Remote = models.BooleanField(default=False)
    image1 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image2 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image4 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image5 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    customerRemarks = models.TextField(null=True, blank=False)
    # customerSignature = models.JSignatureField()

    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING, null=True, blank=True)
    rcNo = models.CharField(max_length=255, null=True, blank=True)

    # def __str__(self):
    #     return self.customerRemarks
