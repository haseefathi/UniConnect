from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/skeleton.html', context)

def dashboard_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/dashboard.html', context)

def predictor_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/predictor.html', context)

def universities_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/universities.html', context)
    
def research_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/research.html', context)

def link1_view(request, *args, **kwargs):
    context = {}
    return render(request, 'portal/link1.html', context)


# welcome view
def welcome_view(request, *args, **kwargs):
    context = {}
    return render(request, 'index.html', context)


# random trial views 
def trial_view(request, *args, **kwargs):
    context = {}
    return render(request, 'trial.html', context)

def fruits_view(request, *args, **kwargs):
    context = {}
    return render(request, 'fruits.html', context)

def veg_view(request, *args, **kwargs):
    context = {}
    return render(request, 'veg.html', context)

