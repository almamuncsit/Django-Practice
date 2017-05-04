from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .models import Video
from .forms import LoginForm
# Create your views here.


def home(request):
    last_video = Video.objects.all().order_by("-id")[0]
    return render(request, 'home.html', {'last_video': last_video})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = form.authenticate()
        if user:
            return redirect('/')
        else:
            return HttpResponse("Login failed or form invalid")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return HttpResponse("User ID " + str(user.id) + " Created")
            else:
                return HttpResponse("Error")
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#
#         if username is not None and password is not None and username != '' and password != '':
#             user = authenticate(username=username, password=password)
#             if user:
#                 return redirect("/")
#             else:
#                 return HttpResponse("Login Failed")
#
#         else:
#             return HttpResponse("Empty Value Detected")
#
#     return render(request, 'login.html')
