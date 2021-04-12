from django.urls import path
from .views import user_signup_view

urlpatterns = [
    path('signup/', user_signup_view, name = 'signup')
]