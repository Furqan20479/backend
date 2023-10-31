from django.shortcuts import render
from django.http import HttpResponse
from .models import Index


def index(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        index = Index(name=name, email=email, phone=phone, desc=desc)
        index.save()
        

    return render(request,'index.html')

