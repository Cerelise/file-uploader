from django.urls import path
from . import views

urlpatterns = [
    path('drf-upload/',views.FilesViewSet.as_view({
      "get":"list",
      "post":"create",
    })),
    path('multiply-upload/', views.multiply_upload, name='multiply_upload')
]