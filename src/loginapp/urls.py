from postapp.views import liked
from django.urls import path
from loginapp.views import *

urlpatterns = [
    path('signup', sign_up, name='sign_up'),
    path('login', login_page, name='login_page'), 
    path('edit-profile', edit_profile, name='edit_profile'),
    path('logout', logout_user, name='logout'), 
    path('profile', profile, name='profile'),
    path('user/<username>', user, name='user', ),
    path('follow/<username>', follow, name='follow', ),
    path('unfollow/<username>', unfollow, name='unfollow', ),

]