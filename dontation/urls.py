
from django.urls import path
from . import views

urlpatterns = [
    path('', views.charity_home, name='home'),
]
