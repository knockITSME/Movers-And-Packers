from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from PM.models import userdetails, CustomerEnquiry
from PM.forms import FormUserdetails
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
 return render(request,'index.html')
def aboutusView(request):
 return render(request,'about.html')
def contactView(request):
 return render(request,'contact.html')
def regformView(request):
 return render(request,'formpage.html')
def servicesView1(request):
 return render(request,'servicetype2.html')
def servicesView2(request):
 return render(request,'servicetype1.html')
def loginView1(request):
 return render(request,'loginpg.html')
def signupView1(request):
 return render(request,'signup.html')
def getaquoteView(request):
 return render(request,'getfreequote.html')
def signupForm(request):
 if request.method == "POST":
  username=request.POST["username"]
 usercontact = request.POST["usercontact"]
 useremail = request.POST["useremail"]
 userpassword=request.POST["userpassword"]
 cpassword = request.POST["cpassword"]
 
 if userpassword==cpassword:
  myuser=User.objects.create_user(username, userpassword)
 myuser.contact=usercontact
 myuser.email=useremail
 myuser.save()
 return render(request,'loginpg.html')




def getquoteForm(request):
  if request.method=="POST":
   cust_name=request.POST["cust_name"]
  cust_email=request.POST["cust_email"]
  cust_contact=request.POST["cust_contact"]
  date=request.POST["date"]
  cust_source=request.POST["cust_source"]
  cust_destination=request.POST["cust_destination"]
  type_of_property=request.POST["type_of_property"]
  cust_note=request.POST["cust_note"]
  
  enquiry_form = CustomerEnquiry(cust_name=cust_name, cust_email=cust_email,cust_contact=cust_contact, date=date, cust_source=cust_source, cust_destination=cust_destination, type_of_property=type_of_property,cust_note=cust_note)
  enquiry_form.save()
    
 
def viewdetails(request):
  customers = CustomerEnquiry.objects.all()
  return render(request,"viewdetails.html",{'customers':customers})

def destroy(request,id):
 print("Customer")
 customer = CustomerEnquiry.objects.get(id=id)
 customer.delete()
 return redirect("/viewdetails")

def handlelogin(request):
 '''context = {}
 if request.method == "POST":
 uname = request.POST['username']
 upassword = request.POST['userpassword']
 rcount=userdetails.objects.filter(username=uname).count()
 if rcount >=1:
 return HttpResponseRedirect(reverse('viewdetails'))
 else:
 context["error"] = "Provide valid credentials !!"
 return render(request, "loginpg.html", context)
 else:
 return render(request, "loginpg.html", context)'''
 if request.method == "POST":
  uname = request.POST['username']
 upassword = request.POST['userpassword']
 user=authenticate(username=uname,password=upassword)
 if user is not None:
  login(request, user)
  return redirect('/')

 else:
   return redirect('/')
 
def handlelogout(request):
  logout(request)
  return render(request, 'loginpg.html')

