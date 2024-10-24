from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_school(request):
    if request.method=='POST':
        sname=request.POST['sn']
        sid=request.POST['sid']
        so=School.objects.get_or_create(school_name=sname,student_id=sid)
        return HttpResponse('data is inserted successfully')
    
    
    return render(request,'insert_school.html')
def insert_student(request):
    sco=School.objects.all()
    d={'sco':sco}
    if request.method=='POST':
        so=request.POST.get('sid')
        slo=School.objects.get(student_id=so)
        sn=request.POST['sn']
        ss=request.POST['ss']
        se=request.POST['se']
        so=Student.objects.get_or_create(student_name=sn,student_section=ss,student_id=slo,student_email=se)
        return HttpResponse('data is successfully entered')
    
    return render(request,'insert_student.html',d)

