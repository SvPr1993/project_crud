from django.urls import path
from app_crud.views import create_views, index_views, edit_views, delete_views

urlpatterns = [
    path('', index_views),
    path('create/', create_views, name='create'),
    path('edit/<int:id>/', edit_views, name='edit'),
    path('delete/<int:id>/', delete_views, name='delete'),
]