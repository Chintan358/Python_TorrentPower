from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):

    studentdata = Studnet.objects.all();

    paginator = Paginator(studentdata, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html',{'studentdata':page_obj})

def viewMarks(request,id):
    marks = Marks.objects.filter(student_id__student_id__student_id=id);

    return render(request, 'viewMarks.html',{'marks':marks,'id':marks[0].student_id.student_id.student_id,'name':marks[0].student_id.name,'email':marks[0].student_id.email});
    