from django.shortcuts import render
from .models import Student
import os
# Create your views here.
def index(request):

    # Fetch all records from the database
    students = Student.objects.all()
    # Add your code here to handle file upload and store it in the database.
    # You can use Django's built-in FileField to handle file uploads.   
    if request.method == 'POST':
       
        name = request.POST['uname']
        file = request.FILES['file']

        Student.objects.create(name=name,image=file)

        return render(request, 'index.html', {'msg': 'File Uploaded Successfully','students':students})


    return render(request, 'index.html', {'title': 'File Upload App','students':students})

def delete(request,id):
    student = Student.objects.get(id=id)
    os.remove(student.image.path)
    student.delete()

    return render(request, 'index.html', {'title': 'File Upload App','msg':'File Deleted Successfully','students':Student.objects.all()})