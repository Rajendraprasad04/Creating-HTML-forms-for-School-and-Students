from django.db import models

# Create your models here.
class School(models.Model):
    school_name=models.CharField(max_length=20)
    student_id=models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.student_id)
class Student(models.Model):
    student_name=models.CharField(max_length=20)
    student_section=models.CharField(max_length=20)
    student_id=models.ForeignKey(School,on_delete=models.CASCADE)
    student_email=models.EmailField()
    def __str__(self):
        return self.student_name
