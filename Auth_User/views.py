from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect,render
from django.contrib.auth import authenticate, login,logout

def do_auth(req):
    if req.method == "POST":
        uname = req.POST.get('username')
        print(uname)
        pas = req.POST.get('password')
        user = None
        try:
            user = User.objects.get(username=uname)
        except Exception as e:
            pass
        if user is not None:
            login(req, user)
            return redirect('/home')
        else:
            print("Invalid credentials")
            return redirect('/login')
            pass
    else:
        return HttpResponse("get request to auth")

def createUser(req):
    if req.method == "POST":
        uname = req.POST.get('username')
        print(uname)
        pas = req.POST.get('password')
        user = None
        try:
            user = User.objects.get(username=uname)
        except Exception as e:
            pass
        if user is not None:
            # login(req, user)
            return redirect('/login')
        else:
            user = User.objects.create_user(username=uname,
                                            password=pas)
            login(req, user)
            print("User is new")
            return redirect('/home')
            pass
    else:
        return HttpResponse("get request to auth")

def test(request):
    return HttpResponse("We are in testMode")

