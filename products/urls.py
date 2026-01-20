from django.urls import path
from . import views

urlpatterns = [
    path('first_blog/', views.korean_products, name='blog_one'),
    path('second_blog/', views.data_time),
    path('third_blog', views.about_myself, name='blog_two'),
    path('saerch/', views.search_view, name='search'),
    path('', views.product, name='home_page'),
    path('product_list/<int:id>/', views.product_detail),
]