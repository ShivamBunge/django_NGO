from . import views
from django.urls import path
urlpatterns = [path("", views.index, name="index"), path("donate", views.donate, name="donate"),path("success", views.success, name="success")]

