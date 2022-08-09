from django.db import models
from applications.categories.models import Category


class Product(models.Model):

    title = models.CharField(
        max_length=100
        )

    image = models.ImageField(
        upload_to='products',
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    active = models.BooleanField(
        default=False
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title
