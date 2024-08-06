from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import adminindex, register, customer_list, movie_list, movie_adding, movie_display, delete_movie, \
    toggle_disable_movie, moviedisplay_details, custom_login, signup, payment_details, \
    payment_success, save_subscription_plan

urlpatterns = [
    path("adminbase/", adminindex, name="adminindex"),
    path("", LoginView.as_view(), name='login'),
    path("adminregister/", register, name="adminregister"),
    path('admincustomer/',customer_list,name="admincustomer"),
    path('adminmovie/',movie_list,name="adminmovie"),
    path('adminadd/',movie_adding,name="adminadd"),
    path('delete_movie/<int:movie_id>/', delete_movie, name='delete_movie'),
    path('toggle_disable_movie/<int:id>/', toggle_disable_movie, name='toggle_disable_movie'),
    path('moviedisplay/',movie_display,name="moviedisplay"),
    path('moviedisplay_details/<int:passed_id>/', moviedisplay_details, name='moviedisplay_details'),
    path('registration/userlogin/', custom_login, name='userlogin'),
    path('signup/', signup,name='signup'),
    path('payment/',payment_details, name='payment'),
    path('subscribe/',save_subscription_plan, name='subscribe'),
    path('payment_success/', payment_success, name='payment_success'),
    path('all/', views.all_movies, name='all_movies'),
    path('anime/', views.anime_movies, name='anime_movies'),
    path('adventure/', views.adventure_movies, name='adventure_movies'),
    path('add_to_watchlist/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
]