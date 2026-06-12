from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Car


class AuthAndCarFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester")

    def test_register_login_and_protected_routes(self):
        protected = reverse("car_list")
        response = self.client.get(protected)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": "new@example.com",
                "password1": "VeryStrongPass123!",
                "password2": "VeryStrongPass123!",
            },
            follow=True,
        )
        self.assertContains(response, "Dashboard")

    def test_car_crud(self):
        self.client.force_login(self.user)

        create = self.client.post(
            reverse("car_create"),
            {
                "make": "Toyota",
                "model": "Corolla",
                "year": 2024,
                "color": "Blue",
                "price": "25000.00",
                "registration_number": "abc123",
            },
            follow=True,
        )
        self.assertContains(create, "Car added successfully")
        car = Car.objects.get()
        self.assertEqual(car.registration_number, "ABC123")
        self.assertEqual(car.price, Decimal("25000.00"))

        update = self.client.post(
            reverse("car_update", args=[car.pk]),
            {
                "make": "Toyota",
                "model": "Camry",
                "year": 2024,
                "color": "Black",
                "price": "26000.00",
                "registration_number": "abc123",
            },
            follow=True,
        )
        self.assertContains(update, "Car updated successfully")
        car.refresh_from_db()
        self.assertEqual(car.model, "Camry")

        delete = self.client.post(reverse("car_delete", args=[car.pk]), follow=True)
        self.assertContains(delete, "Car deleted successfully")
        self.assertEqual(Car.objects.count(), 0)
