from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login,logout

from Task.models import Task

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")

@login_required()
def home_view(request):
    data = Task.objects.filter(user=request.user)
    context = {'todos':data}
    return render(request, "home.html", context)

def logout_view(req):
    logout(req)
    return redirect('/home')

