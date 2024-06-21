from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
def index(request):
    # return HttpResponse("Welcome")
    userdata = User.objects.all()
    return render(request,"index.html",{"userdata":userdata})

def home(request):
    return render(request,"home.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def adduser(request):
    if request.method=='POST':
        id = request.POST['id']
        username = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']

        if id == "":
            User.objects.create(username=username,email=email,phone=phone,age=age)
        else:
            udata = User.objects.get(id = id)
            udata.username=username
            udata.email = email
            udata.phone = phone
            udata.age = age
            udata.save()

    return redirect("index")

def delete(request,id):

    userdata = User.objects.get(id=id)
    userdata.delete()
    return redirect("index")

def edit(request,id):

    user = User.objects.get(id=id)
    userdata = User.objects.all()
    return render(request,"index.html",{"data":user,"userdata":userdata})