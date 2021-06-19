from django.shortcuts import redirect, render, render_to_response

from .forms import SignUpForm, UpdateGradAdmProfileForm

from django.contrib.auth.models import User
from user.models import GraduateAdmissionsProfile, UniversityRecommendation

from django.contrib.auth import authenticate, login

from django.template import RequestContext

from user.university_search import university_search
from user.predict_admissions import get_predictions
from user.recommend_universities import get_recommendations

from connect.models import PublicProfile

import time
from django.http import HttpResponse

def user_signup_view(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            email = request.POST.get('email')
            gender = request.POST.get('gender')

            u = User.objects.create_user(username=username, first_name = first_name, last_name = last_name,email = email, password = password )

            # print(u)

            u.refresh_from_db()
            grad_profile = GraduateAdmissionsProfile()
            grad_profile.gender = gender
            grad_profile.user = u
            grad_profile.save()

            u.refresh_from_db()
            public_profile = PublicProfile()
            public_profile.user = u
            public_profile.save()


            user = authenticate(username=u.username, password=password)
            login(request, user)
            return redirect('user-home')

        else:
            print(form.errors)

    context = {
        'form': form
    }
    
    return render(request, 'registration/signup.html', context)



def update_grad_adm_profile_view(request):

    if request.method == 'POST':
        print('form has been submitted')

        form = UpdateGradAdmProfileForm(request.POST)
        
        if form.is_valid():
            print('form is valid')
            degree = request.POST.get('degree')
            gre_verbal_score = request.POST.get('gre_verbal_score')
            gre_quant_score = request.POST.get('gre_quant_score')
            gre_awa_score = request.POST.get('gre_awa_score')
            toefl_score = request.POST.get('toefl_score')
            intended_semester = request.POST.get('intended_semester')
            undergrad_gpa = request.POST.get('undergraduate_gpa')
            intended_field = request.POST.get('intended_field')

            logged_in_username = request.user.username
            
            user = User.objects.get(username = logged_in_username)
            
            user.refresh_from_db()
            grad_profile = GraduateAdmissionsProfile()
            grad_profile.degree = degree
            grad_profile.gre_verbal_score = gre_verbal_score
            grad_profile.gre_quant_score = gre_quant_score
            grad_profile.gre_awa_score = gre_awa_score
            grad_profile.toefl_score = toefl_score
            grad_profile.intended_semester = intended_semester
            grad_profile.undergrad_gpa = undergrad_gpa
            grad_profile.gender = user.graduateadmissionsprofile.gender
            grad_profile.user = user
            grad_profile.is_profile_updated = True
            grad_profile.intended_field = intended_field
            grad_profile.save()

            # deleting previously saved recommendations
            delete_recommendations(user)

            return redirect('user-home')
            # print(user)
        
        else:
            print(form.errors)
            print('form not valid')

    else:
        current_user = request.user
        initial_values = {}
        if current_user.graduateadmissionsprofile.is_profile_updated:
            initial_values = {
                'degree': current_user.graduateadmissionsprofile.degree, 
                'gre_verbal_score': current_user.graduateadmissionsprofile.gre_verbal_score,
                'gre_quant_score': current_user.graduateadmissionsprofile.gre_quant_score,
                'gre_awa_score': current_user.graduateadmissionsprofile.gre_awa_score,
                'toefl_score':  current_user.graduateadmissionsprofile.toefl_score,
                'intended_semester': current_user.graduateadmissionsprofile.intended_semester,
                'undergraduate_gpa': current_user.graduateadmissionsprofile.undergrad_gpa,
                'intended_field': current_user.graduateadmissionsprofile.intended_field
            }
        form = UpdateGradAdmProfileForm(initial = initial_values)

    context = {
        'form': form
    }


    return render(request, 'registration/update-grad-adm-profile.html', context)


def university_search_view(request):
    college_name = request.GET['college_name']
    context = university_search(college_name)
    return render(request, 'portal/university-search.html', context)



def admissions_predictor_view(request):
    if 'college_name' in request.GET:

        college_name = request.GET['college_name']
        current_user = request.user

        if current_user.graduateadmissionsprofile.is_profile_updated:
            student_info = {
                'profile_updated': True,
                'gre_verbal_score': current_user.graduateadmissionsprofile.gre_verbal_score,
                'gre_quant_score': current_user.graduateadmissionsprofile.gre_quant_score,
                'gre_awa_score': current_user.graduateadmissionsprofile.gre_awa_score,
                'intended_semester': current_user.graduateadmissionsprofile.intended_semester,
                'toefl_score': current_user.graduateadmissionsprofile.toefl_score,
                'undergrad_gpa': current_user.graduateadmissionsprofile.undergrad_gpa,
                'intended_field': current_user.graduateadmissionsprofile.intended_field
            }
        else:
            student_info = {
                'profile_updated': False,
            }

        context = get_predictions(college_name, student_info)
    else:
        context = {
            'error': True,
            'processed': False
        }
    return render(request,'portal/admissions-predictor.html', context)


def delete_recommendations(user):
    user_recs = UniversityRecommendation.objects.filter(user = user)
    if len(user_recs):
        user_recs.delete()
    return


def save_recommendations(rec_dict, user):
    nn_recommendation = rec_dict.get('cnn_recommendation')
    best_knn_recommendation = rec_dict.get('best_knn_recommendation')
    other_recs_dict = rec_dict.get('remaining_recommendations')

    print('saving best recs')
    nn_rec_object = UniversityRecommendation(user = user, recommendation = nn_recommendation['recommendation'], image_url = nn_recommendation['image_link'], recommendation_type = 1 )
    nn_rec_object.save()

    best_knn_object = UniversityRecommendation(user = user, recommendation = best_knn_recommendation['recommendation'], image_url = best_knn_recommendation['image_link'], recommendation_type = 1 )
    best_knn_object.save()

    print('saving other recommendations')
    for rec in other_recs_dict:
        rec_obj = UniversityRecommendation(user = user, recommendation = rec['recommendation'], image_url = rec['image_link'], recommendation_type = 2 )
        rec_obj.save()


def recommendations_already_generated(user):
    recommendations = UniversityRecommendation.objects.filter(user = user)
    return len(recommendations) != 0


def get_generated_recommendations(user):

    all_recommendations = dict()

    top_recs = UniversityRecommendation.objects.filter(user = user, recommendation_type = 1)
    other_recs = UniversityRecommendation.objects.filter(user = user, recommendation_type = 2)

    cnn_recommendation = {
        'recommendation': top_recs[0].recommendation,
        'image_link': top_recs[0].image_url
    }

    best_knn_recommendation = {
        'recommendation': top_recs[1].recommendation,
        'image_link': top_recs[1].image_url
    }

    other_recs_list = list()
    for rec in other_recs:
        dict_obj = dict()
        dict_obj['recommendation'] = rec.recommendation
        dict_obj['image_link'] = rec.image_url
        other_recs_list.append(dict_obj)


    all_recommendations['cnn_recommendation'] = cnn_recommendation
    all_recommendations['best_knn_recommendation'] = best_knn_recommendation
    all_recommendations['remaining_recommendations'] = other_recs_list

    return all_recommendations



def university_recommender_view(request):

    current_user = request.user
    if current_user.graduateadmissionsprofile.is_profile_updated:
        print('student profile updated')
        if not recommendations_already_generated(request.user):
            print('recommendations being generated for the first time')
            student_info = {
                    'profile_updated': True,
                    'gre_verbal_score': current_user.graduateadmissionsprofile.gre_verbal_score,
                    'gre_quant_score': current_user.graduateadmissionsprofile.gre_quant_score,
                    'gre_awa_score': current_user.graduateadmissionsprofile.gre_awa_score,
                    'intended_semester': current_user.graduateadmissionsprofile.intended_semester,
                    'toefl_score': current_user.graduateadmissionsprofile.toefl_score,
                    'undergrad_gpa': current_user.graduateadmissionsprofile.undergrad_gpa,
                    'intended_field': current_user.graduateadmissionsprofile.intended_field
                }
            context = get_recommendations(student_info)
            save_recommendations(context, request.user)
        else:
            print('retrieving already generated recommendations')
            time.sleep(5)
            context = get_generated_recommendations(request.user)

    
    else:
        print('student profile not updated')
        context = {
            'profile_updated': False
        }

    return render(request,'portal/university-recommender.html', context)







