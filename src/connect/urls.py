from django.urls import path, include
from .views import update_public_profile_view, make_profile_public_private, dynamic_user_profile_lookup_view

from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    path('update_public_profile/', update_public_profile_view, name = 'UpdatePublicProfile'),
    path('change_profile_status/', make_profile_public_private, name = 'change_profile_status'),
    path('profile/<str:my_username>/',dynamic_user_profile_lookup_view, name = 'dynamic_user_profile' ), 

    path('chat/', include(django_private_chat_urls)),
]