from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='dashboard'),
    path('actual/<int:aid>/', views.main, name='actual'),
    path('backup/<str:bid>/', views.main, name='backup'),
]
