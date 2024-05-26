from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate

# Create your views here.

def sing_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"Login Successfull")
            return redirect('index')
        else:
            messages.warning(request,'Please Create A user ')
            return redirect('sing_up')

    return render(request,'account/log_in.html')

def log_out(req):
    log_out(req,User)

def sing_up(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        print(first_name)
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request,"This Email Allready Taken!")
            elif User.objects.filter(username=username).exists():
                messages.warning(request,"This UserName is Taken!")

            else:
                user=User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email)
                user.set_password(password)
                user.save()
                messages.success(request,"Registration Successfull ")
                return redirect(sing_in)
        else:
            messages.warning(request,"Password Dose Not Matched!")

    return render(request,'account/sing_up.html',locals())

