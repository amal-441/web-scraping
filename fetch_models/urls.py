from django.urls import path
from .views import fetch_elements_and_download

urlpatterns = [
    # Other routes...
    path('models/', fetch_elements_and_download, name='fetch_elements_and_download'),
]