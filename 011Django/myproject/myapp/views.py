from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Welcome")
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")