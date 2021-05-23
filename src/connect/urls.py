from django.urls import path
from .views import update_public_profile_view, make_profile_public_private

urlpatterns = [
    path('update_public_profile/', update_public_profile_view, name = 'UpdatePublicProfile'),
    path('change_profile_status/', make_profile_public_private, name = 'change_profile_status')
]