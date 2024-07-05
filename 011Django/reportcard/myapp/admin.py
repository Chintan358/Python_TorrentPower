from django.contrib import admin
from .models import *
# Register your models here.

class StudentData(admin.ModelAdmin):
    list_display = ["student_id","name","email","age"]

class Subjectdata(admin.ModelAdmin):
    list_display = ["subject_name"]

class Marksdata(admin.ModelAdmin):
    list_display = ["Student_ID","Student_Name","student_email",'SUBJECT_NAME',"marks"]

    def SUBJECT_NAME(self,obj):
        return obj.subject_name.subject_name
    def Student_ID(self,obj):
        return obj.student_id.student_id
    def Student_Name(self,obj):
        return obj.student_id.name
    def student_email(self,obj):
        return obj.student_id.email
        

admin.site.register(StudnetId)

admin.site.register(Studnet,StudentData)

admin.site.register(Subject,Subjectdata)

admin.site.register(Marks,Marksdata)
