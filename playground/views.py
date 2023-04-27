from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import signup_form_doc
from .utils import pwd_strength
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
# More of a request handler than a front end "view" perspective.
# View function --> Takes a request and returns a response
# Also called an action in other frameworks
# URLs need to be mapped to views


def home(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def verify_doctor(request):
    #return render(request,'home.html')
    '''obj={}
    obj["username"]=request.POST["email_id"]
    obj["first_name"]=request.POST["first_name"]
    obj["last_name"]=request.POST["last_name"]
    obj["nmc_id"]=int(request.POST["nmc_id"])
    obj["state"]=request.POST["state"]
    obj["year"]=request.POST["year"]
    obj["pwd1"]=request.POST["password1"]'''
    if request.method=='POST':
        form=signup_form_doc(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return redirect('signup')
        

    
    #send data to db then send signup succesfull message popup now here we can check pw1trengths and revert 
    #before saving into db after that redirect to home page
    '''if(pwd_strength(obj["pwd1"])):
        redirect('home')
        pass
        #save to db
    else:
        messages.success(request,'Your password is too weak')
        return HttpResponseRedirect(reverse_lazy('signup'))

    return HttpResponseRedirect(reverse_lazy('home'))    
    #if tests dont pass then return the details'''
    
def signup_user(request):
    context={}
    context["form"]=signup_form_doc()
    return render(request,'signup.html',context)

