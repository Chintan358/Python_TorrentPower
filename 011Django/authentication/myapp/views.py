from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def index(request):
    if request.method=='POST':
        uname = request.POST['uname']
        password = request.POST['pass']
        
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, "Invlid credentials")
            return render(request,"index.html")

    return render(request,"index.html")

def reg(request):

    if request.method =='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['pass']
        
        if User.objects.filter(username=uname).exists():
            messages.add_message(request, messages.INFO, "Username Exist !!!")
            return render(request,'reg.html')

        user = User(first_name=fname,last_name=lname,username=uname)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.INFO, "Registration success")
        return render(request,'reg.html')

    return render(request,'reg.html')

@login_required(login_url='/')
def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return render(request,'index.html')