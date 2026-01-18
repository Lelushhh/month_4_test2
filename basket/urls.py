from django.urls import path
from . import views

urlpatterns = [
    path('create_basket/', views.create_basket_view, name='create_basket'),
    path('basket_list/', views.read_basket_view, name='basket_list'),
    path('basket_list/<int:id>/update/', views.update_basket_view, name='update'),
    path('basket_list/<int:id>/delete/', views.delete_basket_view, name='delete'),
]