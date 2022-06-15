from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse

from Task.models import Task
# Create your views here.

def addTodo(req):
    print("we are in todo")
    if req.method == 'POST':
        if req.user.is_authenticated:
            title = req.POST.get('title')
            status = req.POST.get('status')
            print(title, status)
            task = Task(title = title, status = status,user = req.user)
            print("user is auth to add")
            task.save()
            return redirect("/home")
            # return HttpResponseRedirect(reverse('home'))
            pass
        else:
            print("in valid cred")
            return redirect("/login")
            pass
        pass
    else:
        return HttpResponse("Get request to todo")

def deleteTodo(req, id):
    Task.objects.get(pk= id).delete()
    return redirect("/home")
