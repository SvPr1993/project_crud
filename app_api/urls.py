from django.urls import path
from app_api.views import NamelistApi

urlpatterns = [
    path('name_list/', NamelistApi.as_view()),
]