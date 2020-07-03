from django.urls import path, include
from profile_api import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.HelloApiView.as_view())
]
