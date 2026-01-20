from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class HorseTour(models.Model):
    title = models.CharField(max_length=100)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='tours'
    )

    def __str__(self):
        return f"{self.title} ({self.location})"


class TourRegistration(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='tour_registration'
    )
    tour = models.ForeignKey(
        HorseTour,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.tour}"



class CustomUser(User):
    photo = models.ImageField(upload_to='users/')
    phone_number = models.CharField(max_length=15, default="+996")
    GENDER = (
        ('MALE', 'MALE'),
        ("FEMALE", "FEMALE")
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.username
