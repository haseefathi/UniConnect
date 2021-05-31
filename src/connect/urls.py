from django.urls import path
from .views import update_public_profile_view, make_profile_public_private, dynamic_user_profile_lookup_view

urlpatterns = [
    path('update_public_profile/', update_public_profile_view, name = 'UpdatePublicProfile'),
    path('change_profile_status/', make_profile_public_private, name = 'change_profile_status'),
    path('profile/<str:my_username>/',dynamic_user_profile_lookup_view, name = 'dynamic_user_profile' )
]