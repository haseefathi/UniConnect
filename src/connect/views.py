from django.shortcuts import render
from .forms import UpdatePublicProfileForm

# Create your views here.

def update_public_profile_view(request):

    current_user = request.user

    initial_values = {
        'profile': current_user.publicprofile.profile
    }
    form = UpdatePublicProfileForm(request.POST or None, initial = initial_values)
    
    context = {
        'form': form
    }

    return render(request, 'registration/update-public-profile.html', context)

