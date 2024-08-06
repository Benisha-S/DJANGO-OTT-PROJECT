from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import MovieProfile,UserProfile
from django.contrib.auth.models import auth
from .forms import UserRegisterForm
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import MovieProfile
from .middleware import authenticate_customer
def adminindex(request):
    return render(request,'adminbase.html')





def register(request):
    if request.method == 'POST':
        user_reg_form = UserRegisterForm(request.POST)
        if user_reg_form.is_valid():
            new_user = user_reg_form.save(commit=False)
            new_user.set_password(user_reg_form.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/adminregister_done.html',
                          {'user_reg_form':user_reg_form})
    else:
        user_reg_form=UserRegisterForm()
    return render(request,'registration/adminregister.html',
                          {'user_reg_form':user_reg_form})

def customer_list(request):
    query = request.GET.get('q')
    if query:
        users = UserProfile.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(mobile__icontains=query)
        )
    else:
        users = UserProfile.objects.all()
    return render(request, 'admincustomer.html', {'users':users})


import datetime


from datetime import datetime, timedelta


from django.shortcuts import render, redirect
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from datetime import datetime, timedelta


def save_subscription_plan(request):
    if request.method == 'POST':
        plan = request.POST.get('plan')
        if plan:
            # Assuming you have authenticated users and you can access the user through request.user
            user = request.user
            # Assuming UserProfile is your user profile model linked through a OneToOneField or ForeignKey

            # Set expiry date based on the selected plan
            expiry_date = None
            if plan == 'Base Plan':
                expiry_date = datetime.today() + timedelta(days=30)
            elif plan == 'Standard Plan':
                expiry_date = datetime.today() + timedelta(days=90)
            elif plan == 'Premium Plan':
                expiry_date = datetime.today() + timedelta(days=365)

            # Create a new subscription instance and save it
            subscription = Subscription(user=user, subscription_plan=plan, expiry_date=expiry_date)
            subscription.save()

            # Redirect to the payment page or any other page as needed
            return redirect('payment')  # Assuming 'payment' is the name of the URL pattern for the payment page

    # If the request method is not POST or plan is not provided, render the subscription page
    return render(request, 'subscribe.html', {'value': request.user})


def movie_list(request):
    query = request.GET.get('q')
    if query:
        users = MovieProfile.objects.filter(
            Q(title__icontains=query) |
            Q(genres__icontains=query) |
            Q(director__icontains=query)

        )
    else:
        users =MovieProfile.objects.all()
    return render(request, 'adminmovie.html', {'users':users})


from .forms import MovieForm, SignupForm


def movie_adding(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminmovie')  # Redirect to a URL where you list all movies
    else:
        form = MovieForm()
    return render(request, 'useraccount/adminadd.html', {'form': form})
# views.py



from django.shortcuts import render
from .models import MovieProfile

def movie_display(request):
    query = request.GET.get('q')
    if query:
        movies = MovieProfile.objects.filter(
            Q(title__icontains=query) |
            Q(genres__icontains=query) |
            Q(director__icontains=query)

        )
    else:
        movies = MovieProfile.objects.all()

    return render(request, 'moviedisplay.html', {'movies': movies})

from django.shortcuts import render, get_object_or_404
from .models import MovieProfile

def moviedisplay_details(request, passed_id):
    movie_details = get_object_or_404(MovieProfile, id=passed_id)
    return render(request, "moviedisplay_details.html", {'movie_details': movie_details})



@csrf_exempt
def delete_movie(request, movie_id):
    if request.method == 'DELETE':
        movie = get_object_or_404(MovieProfile, id=movie_id)
        movie.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)



def toggle_disable_movie(request, id):
    movie = get_object_or_404(MovieProfile, id=id)
    if request.method == 'POST':
        movie.is_disabled = not movie.is_disabled
        movie.save()
        return JsonResponse({'message': 'Movie status updated successfully.'}, status=200)
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .middleware import authenticate_customer




def custom_logout(request):
    request.session.flush()  # Clear the session
    return redirect('base')


from django.shortcuts import render

def signup_success_view(request):
    return render(request, 'signup_success.html')


def movies(request):
    return render(request, 'movies.html')

from django.shortcuts import render, redirect

from django.contrib import messages
# from .forms import SignupForm, MyLoginForm

from django.shortcuts import render, redirect
from .forms import SignupForm
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribe')  # Replace 'subscribe' with your success URL name
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


from django.shortcuts import render
from django.http import JsonResponse

from django.contrib import messages


def subscribes(request):
    return render(request, 'subscribe.html')


from django.shortcuts import render

def payment_details(request):
    return render(request, 'payment.html')  # Ensure this is the correct path to your template

def payment_success(request):
    return render(request, 'payment_success.html')
from django.shortcuts import render
from .models import MovieProfile

def all_movies(request):
    movies = MovieProfile.objects.all()
    return render(request, 'all_movies.html', {'movies': movies})

def anime_movies(request):
    movies = MovieProfile.objects.filter(genres__icontains='anime')
    return render(request, 'anime_movies.html', {'movies': movies})

def adventure_movies(request):
    movies = MovieProfile.objects.filter(genres__icontains='adventure')
    return render(request, 'adventure_movies.html', {'movies': movies})
from django.shortcuts import render, redirect

from django.shortcuts import redirect
from .models import MovieProfile


def add_to_watchlist(request, movie_id):
    movie = MovieProfile.objects.get(id=movie_id)

    return render(request, 'add_to_watchlist.html', {'movies': movie})  # Assuming 'watchlist' is the name of the URL pattern for the watchlist page

# views.py
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f'Attempting to log in with email: {email}')

        user = authenticate_customer(email, password)
        if user:
            print('User authenticated')
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session.set_expiry(0)  # Expires when the browser is closed

            messages.success(request, f'Welcome {user.username}')
            return redirect('moviedisplay')
        else:
            print('Authentication failed')
            messages.error(request, 'Invalid email or password')

    return render(request, 'registration/userlogin.html')



