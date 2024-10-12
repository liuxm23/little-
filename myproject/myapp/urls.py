from django.urls import path
from .views import random_person

urlpatterns = [
    path('api/random-person/', random_person, name='random_person'),
]