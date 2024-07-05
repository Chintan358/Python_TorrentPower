from django.db import models

# Create your models here.
class StudnetId(models.Model):
    student_id = models.CharField(max_length=50)

   

class Studnet(models.Model):
    student_id = models.ForeignKey(StudnetId,on_delete=models.CASCADE)
    name =  models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    age = models.IntegerField()

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)

class Marks(models.Model):
    student_id = models.ForeignKey(Studnet,on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()

