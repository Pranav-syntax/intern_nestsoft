from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("cars/", views.car_list_view, name="car_list"),
    path("cars/add/", views.car_create_view, name="car_create"),
    path("cars/<int:pk>/edit/", views.car_update_view, name="car_update"),
    path("cars/<int:pk>/delete/", views.car_delete_view, name="car_delete"),
]
