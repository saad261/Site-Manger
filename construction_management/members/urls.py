from django.urls import path
from . import views
from .views import download_pdf

urlpatterns = [
    path('members/', views.members, name='members'),
    path('download/pdf/', download_pdf, name='download_pdf'),
]