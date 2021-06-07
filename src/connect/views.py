from django.shortcuts import redirect, render
from .forms import UpdatePublicProfileForm
from .models import PublicProfile, Friend_Request, Friendships
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User

from datetime import date

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
            print('form isnt valid')
        
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


def make_profile_public_private(request):
    
    user = request.user

    user.refresh_from_db()

    # print('inside make profile status function')
    new_status = request.POST.get('is_public')

    is_public = (new_status == 'true')
    # print('changing status to', is_public)
    # print('old value', user.publicprofile.profile_public)
    # print('changing value now')
    user.publicprofile.profile_public = is_public
    user.publicprofile.save()
    # print('after changing', user.publicprofile.profile_public)
    return HttpResponse('Sucessful')



def connect_home_view(request, *args, **kwargs):

    logged_in_username = request.user.username
    logged_in_user = request.user

    # getting all other users who have set their profiles as public
    other_users = User.objects.exclude(username = logged_in_username)
    
    required_users = list()

    for user in other_users:
        if user.publicprofile.profile_public:
            if not is_friended(logged_in_user, user):
                required_users.append(user)



    def get_available_values(users):
        available_unis = list()
        available_cities = list()
        available_countries = list()
        starting_years = list()

        for user in users:
            if user.publicprofile.accepted_university not in available_unis:
                available_unis.append(user.publicprofile.accepted_university)

            if user.publicprofile.origin_city not in available_cities:
                available_cities.append(user.publicprofile.origin_city)
            
            if user.publicprofile.destination_city not in available_cities:
                available_cities.append(user.publicprofile.destination_city)

            if user.publicprofile.origin_country.name not in available_countries:
                available_countries.append(user.publicprofile.origin_country.name)
            
            if user.publicprofile.destination_country.name not in available_countries:
                available_countries.append(user.publicprofile.destination_country.name)

            if user.publicprofile.starting_year not in starting_years:
                starting_years.append(user.publicprofile.starting_year)

        return available_unis, available_cities, available_countries, sorted(starting_years)

    
    unis, cities, countries, years = get_available_values(required_users)

    

    context = {
        'connect_users': required_users,
        'universities': unis, 
        'cities': cities, 
        'countries': countries,
        'years': years
    }
    
    return render(request, 'portal/home.html', context)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))




def dynamic_user_profile_lookup_view_home(request, my_username):
    # print('username in dynamic view', my_username)
    lookup_user = User.objects.get(username = my_username)

    age = calculate_age(lookup_user.publicprofile.date_of_birth)

    context = {
        'lookup_user': lookup_user, 
        'age': age, 
        'is_friended': is_friended(request.user, lookup_user), 
        'is_requested': is_requested(request.user, lookup_user)
    }

    # print(lookup_user.last_name)
    
    return render(request, 'portal/user_profile_details_home.html', context)


def dynamic_user_profile_lookup_view_friends(request, my_username):
    # print('username in dynamic view', my_username)
    lookup_user = User.objects.get(username = my_username)

    age = calculate_age(lookup_user.publicprofile.date_of_birth)

    context = {
        'lookup_user': lookup_user, 
        'age': age, 
        'is_friended': is_friended(request.user, lookup_user), 
        'is_requested': is_requested(request.user, lookup_user)
    }

    # print(lookup_user.last_name)
    
    return render(request, 'portal/user_profile_details_friends.html', context)



def dynamic_user_profile_lookup_view_request(request, my_username):
    # print('username in dynamic view', my_username)
    lookup_user = User.objects.get(username = my_username)

    age = calculate_age(lookup_user.publicprofile.date_of_birth)

    friend_request = Friend_Request.objects.get(to_user = request.user, from_user = lookup_user)


    context = {
        'lookup_user': lookup_user, 
        'age': age, 
        'is_friended': is_friended(request.user, lookup_user), 
        'is_requested': is_requested(lookup_user, request.user), 
        'friend_request': friend_request
    }

    # print(lookup_user.last_name)
    
    return render(request, 'portal/user_profile_details_request.html', context)


def is_friended(from_user, to_user):
    return Friendships.objects.filter(subject = from_user, friend = to_user).exists()

def is_requested(from_user, to_user):
    return Friend_Request.objects.filter(from_user = from_user, to_user = to_user).exists()


@login_required
def send_friend_request(request):

    print('in send request view')
    from_user = request.user

    to_username = request.POST.get('to_username')
    to_user = User.objects.get(username = to_username)

    friended = is_friended(from_user, to_user)
    print('friended', friended)

    if not friended:    
        print('not friends... sending request')
        # the person is not friends...so send request
        friend_request, created = Friend_Request.objects.get_or_create(from_user = from_user, to_user = to_user)
        if created:
            return HttpResponse('Friend request successfully sent!')
        else:
            return HttpResponse('Friend request already sent!')
    else:
        return HttpResponse('Already friends')




@login_required
def accept_friend_request(request):
    print('in accept view')
    requestID = request.POST.get('request_id')

    print(requestID, type(requestID))

    friend_request = Friend_Request.objects.get(id = requestID)

    if friend_request.to_user == request.user:
        friendship_a2b, created_a2b = Friendships.objects.get_or_create(subject = request.user, friend = friend_request.from_user)
        friendship_b2a, created_b2a = Friendships.objects.get_or_create(subject = friend_request.from_user, friend = request.user)
        friend_request.delete()
        print('request accepted ------------------------------------------')
        return HttpResponse('friend request accepted')
        
    else:
        return HttpResponse('friend request not accepted')


def show_friends(request):

    logged_in_user = request.user

    user_friend_requests = Friend_Request.objects.filter(to_user = logged_in_user)
    user_friends = Friendships.objects.filter(subject = logged_in_user)
    requests_available = (len(user_friend_requests) != 0)
    friends_available = (len(user_friends) != 0 )

    context = {
        'requests': user_friend_requests, 
        'requests_available': requests_available, 
        'friends': user_friends, 
        'friends_available': friends_available
    }

    return render(request, 'portal/user_friends.html', context)



def delete_friend_request(request):
    requestID = request.POST.get('request_id')
    print(requestID,'in view')
    friend_request = Friend_Request.objects.get(id = requestID)
    if friend_request.to_user == request.user:
        friend_request.delete()
        return HttpResponse('friend request deleted')
    else:
        return HttpResponse('something is wrong')










