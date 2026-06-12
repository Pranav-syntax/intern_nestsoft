from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1886), MaxValueValidator(date.today().year + 1)]
    )
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    registration_number = models.CharField(max_length=30, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"
