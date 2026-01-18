from django.db import models
from products.models import Products

class Basket(models.Model):
    name_basket = models.CharField(max_length=100, verbose_name='Enter your name')
    surname = models.CharField(max_length=100, verbose_name='Enter your surname')
    phone_number = models.CharField(max_length=15, verbose_name='Enter your phone number')
    city = models.CharField(max_length=100)

    GENDER = (
        ('MALE', 'MALE'),
        ("FEMALE", "FEMALE")
    )
    gender = models.CharField(max_length=100, choices=GENDER, blank=True)

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='basket_items',
        null=True,
        blank=True
    )
   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.product}'


    class Meta:
      verbose_name = 'tasks'
      verbose_name_plural = 'task'
