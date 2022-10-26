from django.db import models
from django.conf import settings
from accounts.models import User


class Address(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    postal_code = models.BigIntegerField(null=False)
    address_name = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Addresses'
    
    def __str__(self):
        return f"{self.address_line1}, {self.address_line2}, {self.city}, {self.postal_code}, {self.landmark}."
