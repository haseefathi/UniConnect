from django.urls import path, include
from .views import update_public_profile_view, make_profile_public_private, dynamic_user_profile_lookup_view, send_friend_request, accept_friend_request, show_friend_requests, delete_friend_request

from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    path('update_public_profile/', update_public_profile_view, name = 'UpdatePublicProfile'),
    path('change_profile_status/', make_profile_public_private, name = 'change_profile_status'),
    path('profile/<str:my_username>/',dynamic_user_profile_lookup_view, name = 'dynamic_user_profile' ),

    # urls for showing, accepting, sending friend requests, deleting
    path('send_friend_request/',send_friend_request, name = 'send friend request' ), 
    path('accept_friend_request/',accept_friend_request, name = 'accept friend request' ), 
    path('delete_friend_request/',delete_friend_request, name = 'delete friend request' ),
    path('friend_requests/' ,show_friend_requests, name = 'show friend requests' ), 


    # urls for chat
    path('chat/', include(django_private_chat_urls)),
]