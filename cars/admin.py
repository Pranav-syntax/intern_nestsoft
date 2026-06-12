from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "year", "color", "price", "registration_number", "created_by")
    search_fields = ("make", "model", "registration_number")
    list_filter = ("year", "color")
