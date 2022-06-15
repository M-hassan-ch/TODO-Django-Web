from django.urls import path
from .views import *

urlpatterns = [
    path('verify/', do_auth, name='verify'),
    path('createUser/', createUser, name='createUser'),
]
