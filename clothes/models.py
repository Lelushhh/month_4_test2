from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClothesModel(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='clothes/')
    brands = models.ManyToManyField(Brand, related_name='clothes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
