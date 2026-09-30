from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    name = models.CharField(max_length=100, default="BMW")
    model = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vehicles/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.model}"


class TestDriveBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.vehicle}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s profile"