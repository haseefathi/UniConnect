from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'index.html', context)

def predictor_view(request, *args, **kwargs):
    context = {}
    return render(request, 'predictor.html', context)