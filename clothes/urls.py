from django.urls import path
from .views import clothes_list

urlpatterns = [
    path('clothes/', clothes_list, name='clothes'),
]