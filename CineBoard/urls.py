from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view

urlpatterns = [
    path('movie/', views.movie, name='movie'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
    path('movie/add/', views.movie_create, name='movie_add'),
    path('logaut/', auth_views.LogoutView.as_view(), name='logaut'),
    path('logout/', logout_view, name='logout'),
    path('movie/<int:id>/edit/', views.movie_update, name='movie_update'),
    path('movie/<int:id>/delete/', views.movie_delete, name='movie_delete'),
]