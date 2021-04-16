from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/skeleton.html', context)

def dashboard_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/home.html', context)

def predictor_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/predictor.html', context)

def universities_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/universities.html', context)
    
def research_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/research.html', context)

def profile_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/profile.html', context)

# welcome view
def welcome_view(request, *args, **kwargs):
    context = {}
    return render(request, 'index.html', context)
