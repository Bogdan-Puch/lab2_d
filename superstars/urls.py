from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         
    path('star1/', views.star1, name='star1'), 
    path('star2/', views.star2, name='star2'), 
]