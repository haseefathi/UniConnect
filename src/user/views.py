from django.shortcuts import redirect, render

from .forms import SignUpForm, UpdateProfileForm

from django.contrib.auth.models import User
from user.models import SiteUser

from django.contrib.auth import authenticate, login

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
            siteuser = SiteUser()
            siteuser.gender = gender
            siteuser.user = u
            siteuser.save()

            user = authenticate(username=u.username, password=password)
            login(request, user)
            return redirect('user-home')

        else:
            print(form.errors)

    context = {
        'form': form
    }
    
    return render(request, 'registration/signup.html', context)


def update_profile_view(request):
    form = UpdateProfileForm(request.POST or None)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)

        if form.is_valid():
            degree = request.POST.get('degree')
            gre_verbal_score = request.POST.get('gre_verbal_score')
            gre_quant_score = request.POST.get('gre_quant_score')
            gre_awa_score = request.POST.get('gre_awa_score')
            toefl_score = request.POST.get('toefl_score')
            intended_semester = request.POST.get('intended_semester')
            undergrad_gpa = request.POST.get('undergraduate_gpa')

            logged_in_username = request.user.username
            
            user = User.objects.get(username = logged_in_username)
            
            user.refresh_from_db()
            siteuser = SiteUser()
            siteuser.degree = degree
            siteuser.gre_verbal_score = gre_verbal_score
            siteuser.gre_quant_score = gre_quant_score
            siteuser.gre_awa_score = gre_awa_score
            siteuser.toefl_score = toefl_score
            siteuser.intended_semester = intended_semester
            siteuser.undergrad_gpa = undergrad_gpa
            siteuser.user = user
            siteuser.is_profile_updated = True
            siteuser.save()


            return redirect('user-home')
            # print(user)
        
        else:
            print(form.errors)
    context = {
        'form': form
    }

    return render(request, 'registration/update-profile.html', context)
