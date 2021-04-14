from django.urls import path
from .views import user_signup_view, update_profile_view

urlpatterns = [
    path('signup/', user_signup_view, name = 'signup'),
    path('update-profile/', update_profile_view, name = 'update-profile')
]