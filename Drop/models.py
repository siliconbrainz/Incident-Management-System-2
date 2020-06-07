from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Drop(models.Model):
    remarks = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)
    drop_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remarks
