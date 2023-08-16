from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .froms import RegisterForm
from .models import User
# Create your views here.


def register_sender(request):
    if request.method == 'POST': 
      form =RegisterForm(request.POST)
      if form.is_valid():
         var = form.save(commit=False)
         var.sender=True
         var.save()
         messages.success(request,'Account Created Successfuly Login to contenue')
         return redirect('login')
      else:
         messages.warning(request, 'Error Please Check Form')
         return redirect('register_sender')
    else:
       form = RegisterForm()
       return render(request,'register_sender.html', {'form':form})
    


def register_rider(request):
    if request.method == 'POST': 
      form =RegisterForm(request.POST)
      if form.is_valid():
         var = form.save(commit=False)
         var.rider=True
         var.save()
         messages.success(request,'Account Created Successfuly Login to contenue')
         return redirect('login')
      else:
         messages.warning(request, 'Error Please Check Form')
         return redirect('register_rider')
    else:
       form = RegisterForm()
       return render(request,'register_rider.html', {'form':form})
    

def user_login(request):
    if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None and user.is_active:
         login(request,user)
         # Redirect to a success page.
         messages.success(request, f'Your Logged in as {user}')
         return redirect('dashboard')
      else:
        messages.warning(request, 'Error ,invalid cridentials')
        return redirect('login')
    else:
       return render(request, "login.html")
    

def user_logout(request):
   logout(request)
   messages.warning(request,"Logged out successfully!")
   return redirect("login")
