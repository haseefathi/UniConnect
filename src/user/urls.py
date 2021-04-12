from django.urls import path
from .views import SignUpView, user_signup_view

urlpatterns = [
    path('signup/', user_signup_view, name = 'signup')
]