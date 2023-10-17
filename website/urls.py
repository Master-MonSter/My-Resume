from django.urls import path
from website import views

urlpatterns = [
    path('', views.test),
]