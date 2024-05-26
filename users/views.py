from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from . models import User
from . forms import RegisterUserForm
from home.models import Resume


# Create your views here.

def ok(request):
        if request.method =='POST': 
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.username = var.email
                var.save()
                Resume.objects.create(user=var)
                messages.info(request, 'Your account has been created')
                return redirect('login')
            else:
                messages.warning(request, 'Try again')
                return redirect('ok')
        else:
            form = RegisterUserForm()
            context = {'form':form}
            return render(request,"register_applicant.html",context)









def register_applicants(request):  
        if request.method =='POST': 
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.username = var.email
                var.save()
                Resume.objects.create(user=var)
                messages.info(request, 'Your account has been created')
                return redirect('login')
            else:
                messages.warning(request, 'Try again')
                return redirect('register-applicant')
        else:
            form = RegisterUserForm()
            context = {'form':form}
            return render(request,"register_applicant.html",context)



def login_user(request):
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request,user)
            return render(request,'index.html')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('login')
    else:
        return render(request,'login.html')
    



def logout_user(request):
    logout(request)
    messages.info(request,'loged out succesfully')
    return redirect('login')


