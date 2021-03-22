from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html', context)

def predictor_view(request, *args, **kwargs):
    context = {}
    return render(request, 'predictor.html', context)

def link1_view(request, *argsm, **kwargs):
    context = {}
    return render(request, 'link1.html', context)