from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .functions import *
from student.models import *
from student.forms import *
from student.views import *
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def error (request):
    return HttpResponse("<center><h1> There was an Error </h1></center>")
# def welcome(request):
#     return HttpResponse("<center><h1>This is the Welcome Page</h1></center>")
def welcome (request):
    return render(request,'welcome.html')
def tea_home(request):
    return render(request,'teacher/home.html')
def register(request):
    d=registration_form()
    return render(request,"teacher/register.html",{"form":d})
def reg(request):
    a=registration_form(request.POST,request.FILES or None)
    if a.is_valid:
        profileup(request.FILES['profile'])
        a.save()
        messages.success(request,"Registration Success")
        return register(request)
    else:
        messages.warning(request,"Registration Failed")
    return register(request)
def viewcustomers(request):
    id=request.session['id']
    print(id)
    a=registration_model.objects.all().filter(id=id)
    print(a)
    return render(request,"teacher/viewcust.html",{"data":a}) 

# Student and Teacher Details

def teacherdetails(request):
    a=registration_model.objects.all()
    print(a)
    return render(request,"teacher/teacherdetails.html",{'data':a})
def studentdetails(request):
    a=stud_registration_model.objects.all()
    print(a)
    return render(request,"student/studentdetails.html",{'data':a})

                #######
    
    
def del_cust(request):
    a=request.GET["q"]
    print("Id is ",a)
    registration_model.objects.all().filter(id=a).update(status=0)
    return viewcustomers(request)
def edit_cust(request):
    a=request.GET["q"]
    b=registration_model.objects.all().filter(id=a)
    print(b)
    return render(request,'teacher/cust_edit.html',{'data':b})
def edi_cust(request):
    a=request.POST['id']
    b=registration_model.objects.get(id=a)
    print(b)
    c=registration_form(request.POST,request.FILES or None,instance=b)
    if(c.is_valid()):
        profileup(request.FILES['Image'])
        a.save()
        messages.success(request,'Product Updated Successfully')
        return viewcustomers(request)
    else:
        messages.error(request,'Product Updation Failed')
    return viewcustomers(request)

# student view
def stu_view_tea(request):
    b=stud_registration_model.objects.all().filter(status=1)
    return render(request,'teacher/stu_view_tea.html',{'data':b})

# Mark Entry



                        # EDIT STUDENT REGISTER 
# def mark_register(request):
#     a=request.GET["q"]
#     b=stud_registration_model.objects.all().filter(id=a).values("name")
#     name=b[0]["name"]    
#     print(name)  
#     print(b)
#     c=student_marks_register_form()
#     return render(request,'teacher/stu_edi_tea.html',{'form':c,'name':name})
# def mark_reg(request):
#     a=student_marks_register_form(request.POST)
#     if a.is_valid():
#         a.save()
#         messages.success(request,'Marks Registered Successfully')
#         return render(request,'teacher/stu_view_tea.html')
#     else:
#         messages.error(request,'Marks Registration Failed')
#     return render(request,'teacher/stu_view_tea.html')



def mark_register(request):
    a=request.GET["v"]
    
    b=stud_registration_model.objects.all().filter(id=a).values("name","id")
    name=b[0]["name"]
    id=b[0]["id"] 
    return render(request,'teacher/stu_edi_tea.html',{"name":name,"id":id})
def mark_reg(request):
    stu_id=request.GET["stu_id"]
    tam=int(request.GET["tam"])
    eng=int(request.GET["eng"])
    mat=int(request.GET["mat"])
    sci=int(request.GET["sci"])
    soc=int(request.GET["soc"])
    # total=tam+eng+mat+sci+soc
    # per=(total/500)*100
    print(tam)
    print(stu_id)
    data=student_marks_register_model()
    data.stu_id=stu_id
    data.tamil=tam
    data.english=eng
    data.maths=mat
    data.science=sci
    data.social=soc
    # data.total=total
    # data.percentage=per
    data.save()
    return render(request,'teacher/stu_edi_tea.html')

