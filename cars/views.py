from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarForm, RegisterForm
from .models import Car


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect("dashboard")
    return render(request, "registration/register.html", {"form": form})


@login_required
def dashboard_view(request):
    return render(
        request,
        "cars/dashboard.html",
        {"car_count": Car.objects.count()},
    )


@login_required
def car_list_view(request):
    cars = Car.objects.all()
    return render(request, "cars/car_list.html", {"cars": cars})


@login_required
def car_create_view(request):
    form = CarForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        car = form.save(commit=False)
        car.created_by = request.user
        car.save()
        messages.success(request, "Car added successfully.")
        return redirect("car_list")
    return render(request, "cars/car_form.html", {"form": form, "title": "Add Car"})


@login_required
def car_update_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(request.POST or None, instance=car)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Car updated successfully.")
        return redirect("car_list")
    return render(request, "cars/car_form.html", {"form": form, "title": "Update Car"})


@login_required
def car_delete_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car.delete()
        messages.success(request, "Car deleted successfully.")
        return redirect("car_list")
    return render(request, "cars/car_delete_confirm.html", {"car": car})
