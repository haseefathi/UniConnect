from django.urls import path
from .views import update_public_profile_view

urlpatterns = [
    path('update_public_profile/', update_public_profile_view, name = 'UpdatePublicProfile'),
]