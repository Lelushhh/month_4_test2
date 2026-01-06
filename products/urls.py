from django.urls import path
from . import views

urlpatterns = [
    path('first_blog/', views.korean_products),
    path('second_blog/', views.data_time),
    path('third_blog', views.about_myself),
]