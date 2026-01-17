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
        ("Oily", "Oily"),
        ("Masterpiece", "Masterpiece")
    )
    type_products = models.CharField(max_length=100, choices=TYPE_PRODUCT, default="Sweet")
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name_products




class Reviews(models.Model):
    choice_blog = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="review")
    MARKS = (
        ("🌟", "🌟"),
        ("🌟🌟", "🌟🌟"),
        ("🌟🌟🌟", "🌟🌟🌟"),
        ("🌟🌟🌟🌟", "🌟🌟🌟🌟"),
        ("🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟")
    )
    marks = models.CharField(max_length=100, choices=MARKS, default="🌟")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_blog} : {self.marks}'