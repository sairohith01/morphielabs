from django.urls import path
from .views import htopView

urlpatterns = [
    path("htop/", htopView.as_view(), name='htop'),
]