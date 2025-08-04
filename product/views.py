from django.shortcuts import render
from .forms import *
from django.contrib import messages
from .function import *
# Create your views here.
def prod_register(request):
    a=prod_form()
    return render(request,'product/prod_reg.html',{'form':a})
def prod_reg(request):
    a=prod_form(request.POST,request.FILES or None)
    if (a.is_valid()):
        photoupload(request.FILES['Image'])
        a.save()
        messages.success(request,'Product Registered Successfully')
        return prod_register(request)
    else:
        messages.error(request,'Product Registration Failed')
    return prod_register(request)
def prod_view(request):
    b=prod_model.objects.all().filter(status=1)
    return render(request,'product/prod_view.html',{'data':b})
def del_product(request):
    a=request.GET["q"]
    print("Id is ",a)
    prod_model.objects.all().filter(id=a).update(status=0)
    return prod_view(request)
def edi_product(request):
    a=request.GET["q"]
    b=prod_model.objects.all().filter(id=a)
    print(b)
    return render(request,'product/prod_edi.html',{'data':b})
def edi_prod(request):
    a=request.POST['id']
    b=prod_model.objects.get(id=a)
    print(b)
    c=prod_form(request.POST,request.FILES or None,instance=b)
    if(c.is_valid()):
        photoupload(request.FILES['Image'])
        a.save()
        messages.success(request,'Product Updated Successfully')
        return prod_view(request)
    else:
        messages.error(request,'Product Updation Failed')
    return prod_view(request)


