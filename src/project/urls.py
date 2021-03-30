"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, predictor_view, link1_view, dashboard_view, home_view, universities_view, research_view, welcome_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predictor/',predictor_view, name='user-predictor'),
    path('link1/',link1_view, name='user-link1'),
    path('dashboard/',dashboard_view, name='user-dashboard'),
    path('universities/',universities_view, name='user-universities'),
    path('research/',research_view, name='user-research'),
    path('home/',home_view, name='user-home'),

    # the main page when opening site
    path('',welcome_view, name='welcome-page'), 


    # login urls - gives all the authentication views 
    path('user/', include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),

]
