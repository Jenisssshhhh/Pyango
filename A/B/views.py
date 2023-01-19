from django.shortcuts import render,HttpResponse
from .forms import People,Loginform
from .models import User
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    l =Loginform()
    return render(request,'login.html',{"form":l})
    
def register(request):
    if request.method == "POST":
        j = People(request.POST)
        if j.is_valid():
            fn = j.cleaned_data['First_name']
            ln = j.cleaned_data['Last_name']
            e = j.cleaned_data['Email']
            p = j.cleaned_data['Password']
            m = User(First_name = fn ,Last_name = ln, Email = e, Password = p)
            m.save()
            return render(request,'Welcome.html',{'o':fn})
    else:
        j = People()
    return render(request,'register.html',{'form':j})
    