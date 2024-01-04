from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def homepage(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Password is not same")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
        
    return render(request,'sign.html')
    

def login(request):
   if request.method=='POST':
       username=request.POST.get('username')
       pass1=request.POST.get('pass')
       user=authenticate(request,username=username,password=pass1)
       if user is not None:
        return redirect('homepage')
       else:
           return HttpResponse("username and password is incorrect")
   return render(request,'login.html')

def logout(request):
    return redirect('login')