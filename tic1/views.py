from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def signup(request):
    if request.method=='GET':
        context = {
            'form':SignupForm(),
        }
        return render(request,'signup.html',context)
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"succesfully saved")
            messages.success(request,"now you can login")
            return redirect('login')
        else:
            return render(request,'signup.html',{'form':form})


def signin(request):
    if request.method=='GET':
        context = {'form':LoginForm()}
        return render(request,'login.html',context)
    else:
        us = request.POST.get('username')
        pa = request.POST.get('password')
        user = authenticate(username=us,password=pa)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"The credential you entered did not match")
            return render(request,'login.html',{'form':LoginForm()})


@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')