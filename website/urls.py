from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('portfolio-details', views.pDetail_view, name="portfolio-details")
]