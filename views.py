from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . models import supp_reg_table,pdt_reg_tbl
from GUE_Employee.models import emp_reg_tbl

# Create your views here.
from django.http import HttpResponse
# # Create your views here.
# from . models import reg_tbl


def emp_register(request):
     if request.method=="POST" :
        empname=request.POST.get("name")
        age = request.POST.get("age")
        designation = request.POST.get("des")
        gender= request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        dept= request.POST.get("dept")
        dtime=request.POST.get("dtime")
        #empsalary=request.POST.get("salary")
        uname = request.POST.get("uname")
        passwd = request.POST.get("pass")
        obj1=emp_reg_tbl(empname=empname,age=age,designation=designation,gender=gender,email=email,phone=phone,dept=dept,dtime=dtime,
                       uname=uname,passwd=passwd)
        obj1.save()
        if obj1:
          msg="saved successfully"
          return render(request,"Employee_Reg.html",{"reg":msg})
     else:
        return render(request,"Employee_Reg.html")

   #return render(request, "signup.html")
def reg(request):
    return render(request,'Employee_Reg.html')
#def index(request):
#    return render(request,'index.html')
#def vi(request):
 #   viobj = reg_tbl.objects.all()
  #  return render(request,'viewdata.html',{'data':viobj})



### supplier registration......

def supplier_reg(request):
    if request.method == "POST" :
        supName = request.POST.get("supName")
        contact = request.POST.get("contact")
        payment = request.POST.get("payment")
        obj2 = supp_reg_table(supName=supName,contact=contact,payment=payment)
        obj2.save()
        if obj2:
            msg = "saved successfully"
            return  render(request,"Supplier_Reg.html",{"reg":msg})
    else:
        return  render(request,"Supplier_Reg.html")

def product_reg(request):
    if request.method == "POST" :
        pdtname = request.POST.get("pdtname")
        pdtimage = request.FILES.get("pdtimage")
        pdtprice = request.POST.get("pdtprice")
        pdttax = request.POST.get("pdttax")
        pdtquality = request.POST.get("pdtquality")
        pdtstatus = request.POST.get("pdtstatus")
        obj2 = pdt_reg_tbl(pdtname=pdtname,pdtimage=pdtimage,pdtprice=pdtprice,pdttax=pdttax,pdtquality=pdtquality,pdtstatus=pdtstatus)
        obj2.save()
        if obj2:
            msg = "saved successfully"
            return  render(request,"Product_Reg.html",{"reg":msg})
    else:
        return  render(request,"Product_Reg.html")


#view Employee data (fetching)
def viemp(request):
    viobj = emp_reg_tbl.objects.all()
    return render(request,'Emp_reg_view.html',{'data':viobj})

#view supplier details(fetching data)
def visup(request):
    viobj = supp_reg_table.objects.all()
    return render(request,'Sup_reg_view.html',{'data':viobj})


#def index(request):
 #   return render(request,"index.html")
