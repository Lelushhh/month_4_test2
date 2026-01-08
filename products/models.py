from django.db import models


class Products(models.Model):
    name_products = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    TYPE_PRODUCT = (
        ("Sweet", "Sweet"),
        ("Spicy", "Spicy"),
        ("Salty", "Salty"),
        ("Sour", "Sour"),
        ("Oily", "Oily")
    )
    type_products = models.CharField(max_length=100, choices=TYPE_PRODUCT, default="Sweet")
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_products
