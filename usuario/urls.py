from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='usuario'),
    path('create/', views.create, name='usuario_create'),
]