from django.db import models
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from accounts.models import User
from address.models import Address


class OrderItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def getItemTotal(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return self.name

class Payment(models.Model):
    paymentId = models.CharField(max_length=50)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paymentId

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)
    startedDate = models.DateTimeField(auto_now_add=True)
    orderedDate = models.DateTimeField(blank=True, null=True)
    payment = models.ForeignKey(Payment, blank=True, on_delete=models.DO_NOTHING, null=True)
    shippingAddress = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)

    def getItemsCount(self):
        return self.items.aggregate(quantitySum=Sum('quantity'))['quantitySum']

    def getOrderTotal(self):
        total = self.items.aggregate(priceSum=ExpressionWrapper(
            Sum(F('price') * F('quantity')), output_field=DecimalField()))['priceSum']
        return round(total, 2)

    def __str__(self):
        return str(self.id)
