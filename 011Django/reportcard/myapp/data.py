from .models import *
from faker import Faker
fake = Faker()
import random
def setdata(n=10):
    for i in range(n):
        name = fake.name()
        email = fake.email()
        age = random.randint(20,30)
        student_id =f"std_{random.randint(100,999)}"
        std= StudnetId.objects.create(student_id=student_id)

        Studnet.objects.create(name=name, email=email, age=age, student_id=std)


def addMarks():

    for std in Studnet.objects.all():
        for sub in Subject.objects.all():
            Marks.objects.create(student_id=std,subject_name=sub,marks=random.randint(1,100))
