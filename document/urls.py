from django.urls import path
from . import views

urlpatterns = [
    path('multiply-upload/', views.multiply_upload, name='multiply_upload')
]