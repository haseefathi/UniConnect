from django.shortcuts import redirect, render

from .forms import SignUpForm

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

