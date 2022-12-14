from django.db import models
from applications.tables.models import Table
from applications.products.models import Product
from applications.payments.models import Payment


StatusEnum = (
    ('PENDING', 'Pending'), 
    ('DELIVERED', 'Delivered'),
    )


class Order(models.Model):

    table = models.ForeignKey(
        Table, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, null=True, blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=StatusEnum,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    close = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table)
        