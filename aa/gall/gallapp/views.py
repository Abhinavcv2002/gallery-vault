from django.shortcuts import render,redirect
from .models import Gallery
from django.contrib.auth import authenticate, login, logout as authlogout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both username and password are required")
            return render(request, 'signin.html')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            messages.error(request, "invalid")

    return render(request, 'signin.html')

def index(request):
    return render(request, 'index.html')

def usersignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirmpassword = request.POST.get('confirmpassword')
        print(username,email,password,confirmpassword)
    

        if password != confirmpassword:
            print("hello1")
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        try:
            print("hello2")
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('signin')
        except Exception as e:
            print("hello3")
            return render(request, 'signup.html', {'error': str(e)})
    
    return render(request, 'signup.html')

def viewsmain(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    
    if request.method == "POST":
        imgdef = request.FILES['files']
        
        obj = Gallery(pic=imgdef, User=request.user)
        obj.save()
        return redirect(viewsmain)

    imagefeeds = Gallery.objects.filter(User=request.user) 
    return render(request, "index.html", {"feeds": imagefeeds})

def delete(request,pk):
    imagefeeds=Gallery.objects.get(pk=pk)
    imagefeeds.delete()
    return redirect(viewsmain)

def add(request):
    return render(request,'imgadd.html')

def picture(request,id):
    imagefeeds=Gallery.objects.get(pk=id)
    feeds = imagefeeds.pic.url
    return render(request,'imageadd.html',{"feeds":feeds})

def images(request,pk):
    img=Gallery.objects.get(pk=pk)

def logout(request):
    authlogout(request)
    return redirect('../')