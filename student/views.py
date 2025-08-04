from django.shortcuts import render
from .forms import *
from product.models import *
from student.models import *
from django.contrib import messages
from .function import *
# Create your views here.
 #pali
def home(request):
     return render(request,'home.html')

def stu_home(request):
    return render(request,'student/home.html')   

 #login 

def login(request):
    a=Login_form
    return render(request,'adlogin.html',{"form":a})
def adlogin(request ):
    a=Login_form(request.POST)
    if a.is_valid():
        uname=request.POST['UserName']
        passw=request.POST['Password']
        mem=request.POST['Member']
        print("member",mem)
        if(mem=="Teacher"):
            c=registration_model.objects.all().filter(teacher_name=uname,mobile=passw).values("id","mobile","mail","teacher_name")
            if not c:
                messages.warning(request,"Invalid UserName or Password")
                return login(request)
            else:
                id=c[0]["id"]
                mobile=c[0]["mobile"]
                name=c[0]["teacher_name"]
                email=c[0]["mail"]
                request.session["id"]=id
                request.session["Mobile"]=mobile
                request.session["name"]=name
                request.session["mail"]=email
                return render(request,'teacher/home.html')
        elif(mem=="Student"):
            a=stud_registration_model.objects.all().filter(your_reister_no_is=uname,date_of_birth=passw).values("id","name","mail")
            if not a:
                messages.warning(request,"Invalid UserName or Password")
                return login(request)
            else:
                id=a[0]["id"]
                name=a[0]["name"]
                email=a[0]["mail"]
                request.session["id"]=id
                request.session["name"]=name
                request.session["email"]=email
                return render(request,'student/home.html')
        elif(mem=="Admin"):
            if(uname=="admin" and passw=="1234"):
                return render(request,'home.html')
            else:
                return render(request,'adlogin.html')
            
    return login(request)







# View Student
def stu_view(request):
    name=request.session["name"]
    print(name)
    b=stud_registration_model.objects.all().filter(name=name)
    return render(request,'student/stu_view.html',{'data':b})
    
    # Using SESSION
def p_home(request):
    uid=request.session["id"]
    mobile=request.session["mobile"]
    name=request.session["name"]
    email=request.session["email"]
    return render(request,'student/stu_view.html',{"id":uid,"mobile":mobile,"name":name,"email":email})


def p_profile(request):
    uid=request.session["id"]
    mobile=request.session["mobile"]
    name=request.session["name"]
    email=request.session["email"]
    d=prod_model.objects.all().filter(id=uid).values("id","name","mobile","email")
    return render(request,'product/profile.html',{"data":d})
def p_products(request):
    uid=request.session["id"]
    mobile=request.session["mobile"]
    name=request.session["name"]
    email=request.session["email"]
    return render(request,'product/products.html')


#  Student Registeration

def stud_registration(request):
    a=stud_registration_form()
    return render(request,'student/stud_reg.html',{"form":a})

def stud_reg(request):
    a=stud_registration_form(request.POST,request.FILES or None)
    if a.is_valid():
        photoupload(request.FILES['profile'])
        a.save()
        messages.success(request,'Product Registered Successfully')
        return stud_registration(request)
    else:
        messages.warning(request,'Invalid Data')
    return stud_registration(request)
    

# Student view Marks

def stu_view_marks(request):
    id=request.session["id"]
    print(id)
    name=request.session["name"]
    print(name)
    a=student_marks_register_model.objects.all().filter(stu_id=id).values("id","stu_id","tamil","english","maths","science","social","date")
    return render(request,'student/stu_view_marks.html',{"data":a,"name":name})
  
  
  
  
  
  
  
  
  
  
  
 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
   # a=request.POST['tx1']
    # b=request.POST['tx2']
    # if(a=="admin" and b=="1234"):
    #     return render( request,'home.html')
    # else:
    #     return render(request,'adlogin.html')
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

def pali(request):
    return render (request,'pali.html')
def palin(request):
    a=request.POST['tx1']
    b=(a[::-1])
    if (b==a):
        print("It is an Palindrome Number")
        return render (request,'pali.html',{"ans":"It is an Palindrome Number"})
    else:
        print("It is not an Palindrome Number")
        return render(request,'pali.html',{"ans":"It is not an Palindrome Number"})
    
    #calc
    
def calc(request):
    return render (request,'calc.html')
def cal(request):
    a=int(request.POST['tx1'])
    b=int(request.POST['tx2'])
    d=request.POST['dr']
    if(d=="Addition"):
        c=a+b
        v="Addition value is "+str(c)
        print(c)
        return render(request,'calc.html',          )
    elif(d=="Subraction"):
        c=a-b
        print(c)
        return render(request,'calc.html',{"ans":["Subraction Value is",c]})
    elif(d=="Multiplication"):
        c=a*b
        print(c)
        return render(request,'calc.html',{"ans":["Multiplication Value is",c]})
    elif(d=="Division"):
        c=a/b
        print(c)
        return render(request,'calc.html',{"ans":["Division Value is",c]})
    
    
    
    #perfect
    
def perfect(request):
    return render (request,'perfect.html')
def per(request):
    a=int(request.POST['tx1'])
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum=sum+i
    if(sum==a):
        print("It is an Perfect Number")
        return render(request,'perfect.html',{"ans":"It is an Perfect Number"})
    else:
        print("It is not an Perfect Number")
        return render (request,'perfect.html',{"ans":"It is not an Perfect Number"})
    
    
#fibonacci

def fibo(request):
    return render (request,'fibo.html')
def fib(request):
    a=int(request.POST['tx1'])
    s=[]
    n1,n2=0,1
    s.append(0)
    s.append(1)
    for i in range(0,a-2):
        n3=n1+n2
        n1=n2
        n2=n3 
        
        s.append(n3)
        # print(s)
    return render (request,'fibo.html',{"ans":s})