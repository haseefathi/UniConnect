from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'newnavbar.html', context)

def dashboard_view(request, *args, **kwargs):
    context = {}
    return render(request, 'dashboard.html', context)

def predictor_view(request, *args, **kwargs):
    context = {}
    return render(request, 'predictor.html', context)

def universities_view(request, *args, **kwargs):
    context = {}
    return render(request, 'universities.html', context)
    
def research_view(request, *args, **kwargs):
    context = {}
    return render(request, 'research.html', context)

def link1_view(request, *args, **kwargs):
    context = {}
    return render(request, 'link1.html', context)



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

