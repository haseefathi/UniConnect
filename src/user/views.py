from django.shortcuts import redirect, render, render_to_response

from .forms import SignUpForm, UpdateGradAdmProfileForm

from django.contrib.auth.models import User
from user.models import GraduateAdmissionsProfile

from django.contrib.auth import authenticate, login

from django.template import RequestContext




def user_profile_view(request):
    pass

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

    form = UpdateGradAdmProfileForm(request.POST or None)
    print('inside form view')
    if request.method == 'POST':
        form = UpdateGradAdmProfileForm(request.POST)
        print('inside method == post')
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
        print('form not in post')

    context = {
        'form': form
    }


    return render(request, 'registration/update-grad-adm-profile.html', context)
