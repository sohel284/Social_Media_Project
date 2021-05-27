from django.urls import path
from postapp.views import *


urlpatterns = [
    path('', home, name='home'),
    path('like/<pk>', liked, name='liked'),
    path('unlike/<pk>', unliked, name='unliked'),

]