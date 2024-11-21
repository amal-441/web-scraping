# myapp/urls.py
from django.urls import path
from .views import login_and_save_cookies

urlpatterns = [
    path('login/', login_and_save_cookies, name='login_and_save_cookies'),
]
