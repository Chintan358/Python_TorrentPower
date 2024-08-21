from django.shortcuts import render,HttpResponse
from .models import *
from .serialiser import *
# Create your views here.
def getusers(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return HttpResponse(serializer.data)
    
    