from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request, "simpleLoginApp/index.html")

def signup(request):

  if request.method == "POST":
    username = request.POST.get('username')
    fname = request.POST['fname'] # Also like this
    lname = request.POST['lname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    myuser = User.objects.create_user(username, email, pass1)
    myuser.first_name = fname
    myuser.last_name = lname

    myuser.save()
    
    messages.success(request, "Your account has been succesfully created. ")

    return redirect("signin")


  return render(request, "simpleLoginApp/signup.html")

def signin(request):
  return render(request, "simpleLoginApp/signin.html")

def signout(request):
  # return render(request, "simpleLoginApp/signout.html")
  pass
