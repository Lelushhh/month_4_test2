from django.urls import path
from . import views

urlpatterns = [
    path('first_blog/', views.korean_products),
    path('second_blog/', views.data_time),
    path('third_blog', views.about_myself),

    path('product_list/', views.product),
    path('product_list/<int:id>/', views.product_detail),
]