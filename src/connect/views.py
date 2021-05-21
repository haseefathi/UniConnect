from django.shortcuts import render

# Create your views here.

def update_public_profile_view(request):
    context = {}

    return render(request, 'registration/update-public-profile.html', context)
