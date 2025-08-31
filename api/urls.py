from django.urls import path
from .views import GenerateImageAPIView

urlpatterns = [
    path("generate/", GenerateImageAPIView.as_view(), name="generate_image"),
]
