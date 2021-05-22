from django.shortcuts import redirect, render
from .forms import UpdatePublicProfileForm
from .models import PublicProfile

# Create your views here.

def update_public_profile_view(request):

    if request.method == 'POST':
        print('public prof form has been submitted')
        form = UpdatePublicProfileForm(request.POST)

        if form.is_valid():
            print('public prof form is valid')
            degree = request.POST.get('degree')
            starting_semester = request.POST.get('starting_semester')
            major = request.POST.get('major')
            profile = request.POST.get('profile')
            date_of_birth = request.POST.get('date_of_birth')

            origin_city = request.POST.get('origin_city')
            origin_country = request.POST.get('origin_country')
            destination_city = request.POST.get('destination_city')
            destination_country = request.POST.get('destination_country')

            accepted_university = request.POST.get('accepted_university')

            starting_year = request.POST.get('starting_year')

            user = request.user

            user.refresh_from_db()

            public_profile = PublicProfile()

            public_profile.degree = degree
            public_profile.starting_semester = starting_semester
            public_profile.major = major
            public_profile.profile = profile
            public_profile.date_of_birth = date_of_birth
            public_profile.origin_city = origin_city
            public_profile.origin_country = origin_country
            public_profile.destination_city = destination_city
            public_profile.destination_country = destination_country
            public_profile.accepted_university = accepted_university
            public_profile.profile_updated = True
            public_profile.starting_year = starting_year
            public_profile.user = user
            public_profile.save()


            return redirect('user-home')
        
        else:
            print(form.errors)
            print('form is not valid')
        
    else:

        current_user = request.user
        # print(dir(current_user))
        initial_values = {}
        # print('******************* initial form loaded for people without initial values ****************')
        if current_user.publicprofile.profile_updated:
            initial_values = {
                'profile': current_user.publicprofile.profile,
                'date_of_birth': current_user.publicprofile.date_of_birth, 
                'origin_city': current_user.publicprofile.origin_city,
                'origin_country': current_user.publicprofile.origin_country,
                'destination_city': current_user.publicprofile.destination_city,
                'destination_country': current_user.publicprofile.destination_country,
                'accepted_university': current_user.publicprofile.accepted_university, 
                'major': current_user.publicprofile.major, 
                'starting_semester': current_user.publicprofile.starting_semester, 
                'starting_year': current_user.publicprofile.starting_year, 
                'degree': current_user.publicprofile.degree
            }
        form = UpdatePublicProfileForm(request.POST or None, initial = initial_values)
        
    context = {
        'form': form
    }

    return render(request, 'registration/update-public-profile.html', context)

