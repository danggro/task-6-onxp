from django.urls import path

from . import views

urlpatterns = [
    path("blogs/", views.blogs),
    path("login/", views.login),
    ]

