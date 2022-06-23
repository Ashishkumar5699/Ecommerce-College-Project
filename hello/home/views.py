from multiprocessing import context
import django
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

from django.test import RequestFactory
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .models import Product
from math import ceil
 

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4)) 
    params = {'no_of_Slides': nSlides, 'range':range(1, nSlides), 'product':products}  
    return render(request, "index.html", params)

def about(request):
    return render(request, "about.html")

def Contact_page(request):
    # Hello comments
    return render(request, "contact.html")

def Querrysubmit(request):
    if request.method == "POST":
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_phone = request.POST.get('phone')
        contact_desc = request.POST.get('desc')   
        contact_submit = Contact(Name = contact_name, Email = contact_email, Phone = contact_phone, Desc = contact_desc, Date = datetime.today())
        contact_submit.save()
        messages.success(request, 'your message has been send.')
        return render(request,"submit_contact.html")

def order(request):
    return render(request,"order.html")

def repairing(request):
    return render(request,"repairing.html")

def mortgage(request):
    return render(request,"mortgage.html")

def checkout(request):
    return render(request, "checkout.html")

def services(request):
    return render(request, "services.html")

def loginUser(request):
    if request.method == "POST":
        user_name = request.POST.get("usernameEntry")
        pass_word = request.POST.get("passwordEntry")
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            # django.contrib.auth.
            login(request, user)
            return redirect("http://127.0.0.1:8000/")
        else:
            return HttpResponse("something wents wrong")

    return render(request, "login.html")

                
def logoutUser(request):
    logout(request)
    return redirect("/login")

def CreateNewAccount(request):
    if request.method == "POST":
        NameEntry = request.POST.get("NameEntry")
        emailEntry = request.POST.get("emailEntry")
        phoneEntry = request.POST.get("phoneEntry")
        username = request.POST.get("username")
        password = request.POST.get("password")

        

        return render(request, "CreateNewAccount.html")

def tracker(request):
    return render(request, "tracker.html")

def productview(request):
    return render(request, "productview.html")

def checkout(request):
    return render(request, "checkout.html")
