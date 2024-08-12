from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
    

def loadstudents(request):
    students = Studnet.objects.all()
    return JsonResponse({"Students":list(students.values())})
    

def addstudent(request):
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    # Save the data to the database
    # ... 
    Studnet.objects.create(name=name,email=email,age=age)

    return HttpResponse("Data inserted successfully")

def deleteStudent(request):
    id = request.GET.get('id')
    Studnet.objects.filter(id=id).delete()
    return HttpResponse("Data deleted successfully")

def getStudent(request):
    id = request.GET.get('id')
    student = Studnet.objects.filter(id=id)
    return JsonResponse({"Student":list(student.values())})

def editStudent(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    student = Studnet.objects.get(id=id)
    student.name=name
    student.email=email
    student.age=age

    student.save()
    

    return HttpResponse("Data Updated successfully")

def searchstudent(request):

    search_query = request.GET.get('value')
    students = Studnet.objects.filter(name__startswith=search_query)
    return JsonResponse({"Students":list(students.values())})