from django.urls import path
from .views import user_signup_view, update_grad_adm_profile_view, university_search_view,admissions_predictor_view, university_recommender_view

urlpatterns = [
    path('signup/', user_signup_view, name = 'signup'),
    path('update-grad-adm-profile/', update_grad_adm_profile_view, name = 'update-grad-adm-profile'),
    path('university-search/', university_search_view, name = 'university-search'),
    path('university-admissions-predictor/', admissions_predictor_view, name = 'admissions-predictor'),
    path('university-recommender/', university_recommender_view, name = 'university-recommender'),

]