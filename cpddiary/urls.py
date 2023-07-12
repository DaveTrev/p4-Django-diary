from django.urls import path
from . import views

urlpatterns = [
    path('cpddiary/', views.cpddiary, name="cpddiary"),
]