from django.shortcuts import render
from .models import user
from django.core.paginator import Paginator
from .models import Song
from django.contrib import messages
from django.http import HttpResponse


def log(request):
    return render(request,"MusicApp/log.html")

def register(request):
    return render(request,"MusicApp/register.html")
    
def sign(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    pass1 = request.POST['password1']
    pass2 = request.POST['password2']

    if user.objects.filter(email=email).exists():
        messages.success(request, "Email is already registered.")
    else:
        if pass1 != pass2:
            messages.success(request, "Password is not matching.")
        else:
            new_user = user.objects.create(user=name, email=email, phone=phone, password=pass1)
            new_user.save()
            return render(request,"MusicApp/log.html")
    return render(request,"MusicApp/register.html")

def index(request):
    email = request.POST['mail']
    passwd = request.POST['password']

    usercheck = user.objects.get(email=email)
    if usercheck.password == passwd:
        songs = Song.objects.all()

        context = {
            'songs': songs,
            }
        return render(request,"MusicApp/index.html",context)
    else:
        messages.success(request, "Username or Password Incorrect")
    return render(request,"MusicApp/log.html")
    

    
    
    

    

