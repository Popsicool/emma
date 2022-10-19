from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'transactions'
urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard', views.dashboard.as_view(), name="dashboard"),
]