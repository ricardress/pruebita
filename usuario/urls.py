from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='usuario'),
    path('create/', views.create, name='usuario_create'),
    path('edit/<int:id>', views.edit, name='usuario_edit'),
    path('delete/<int:id>', views.delete, name='usuario_delete')
]