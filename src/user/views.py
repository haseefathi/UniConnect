from django.shortcuts import redirect, render, render_to_response

from .forms import SignUpForm, UpdateGradAdmProfileForm

from django.contrib.auth.models import User
from user.models import GraduateAdmissionsProfile

from django.contrib.auth import authenticate, login

from django.template import RequestContext

from user.university_search import university_search
from user.predict_admissions import get_predictions
from user.recommend_universities import get_recommendations

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

            return redirect('user-home')
            # print(user)
        
        else:
            print(form.errors)
            print('form not valid')

    else:
        form = UpdateGradAdmProfileForm()

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


def university_recommender_view(request):

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
        print(student_info)
        context = get_recommendations(student_info)
    return render(request,'portal/university-recommender.html', context)







