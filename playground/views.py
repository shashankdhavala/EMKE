from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import signup_form_doc,signup_form_patient,doctor_login
from .models import Doctor,Patient
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


def verify_login(request):
    form=doctor_login(request.POST)
    doc_username=str(request.POST['username'])
    password=str(request.POST['password'])
    #return HttpResponse("hello"+doc_username)
    #check from db

    #data=Doctor.objects.raw('select password from doctor where username=%s',[doc_username])
    data=Doctor.objects.filter(email_id=doc_username)
    if data:
        passw=data[0].password
    else:
        passw=' '
    
    verified=False

    if passw==password:
        verified=True
        
    if verified:
        doc={}
        doc["id"]=data[0].doctor_id
        return render(request,'doc_home.html',doc)    
    else:
        messages.success(request,'Your credentials are wrong')
        return HttpResponseRedirect(reverse_lazy('login'))
    


    

def verify_doctor(request):
    #return render(request,'home.html')
    #generate uuid before saving
    #how to save without using form
    #check if username is already in use
    if request.method=='POST':
        form=signup_form_doc(request.POST)
        password=str(request.POST['password'])
        #if form.is_valid():
        if(pwd_strength(password)):
            form.save()
            return redirect('home')
        else:
            messages.success(request,'Your password is too weak')
            return HttpResponseRedirect(reverse_lazy('signup'))

        return redirect('signup')
        

    return HttpResponseRedirect(reverse_lazy('home'))    
    #if tests dont pass then return the details'''

def save_patient(request):
    #return HttpResponse(request)
    #fill doctor id
    doc_id=request.POST["id"]
    if request.method=='POST':
        form=signup_form_patient(request.POST)
        doc_obj=Doctor.objects.get(doctor_id=doc_id)
        model_object=Patient(first_name=request.POST["first_name"],last_name=request.POST["last_name"],Age=request.POST["Age"],Gender=request.POST["Gender"],doctor_id=doc_obj)

        model_object.save()
        info={}
        info["id"]="id"
        return render(request,'doc_home.html',info)
        #uuid gen
        #query docid
def add_patient(request):
    #return HttpResponse(request)
    context={}
    context["id"]=request.POST["id"]
    context["form"]=signup_form_patient()
    return render(request,'add_patients.html',context)

def view_patients(request):
    return HttpResponse(request)

def login_doctor(request):
    context={}
    context["form"]=doctor_login()
    return render(request,'login.html',context)

def signup_doctor(request):
    context={}
    context["form"]=signup_form_doc()
    return render(request,'doctor_signup.html',context)

def signup_patient(request):
    context={}
    context["form"]=signup_form_patient()
    return render(request,'',context)

