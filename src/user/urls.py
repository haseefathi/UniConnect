from django.urls import path
from .views import user_signup_view, update_grad_adm_profile_view

urlpatterns = [
    path('signup/', user_signup_view, name = 'signup'),
    path('update-grad-adm-profile/', update_grad_adm_profile_view, name = 'update-grad-adm-profile')
]