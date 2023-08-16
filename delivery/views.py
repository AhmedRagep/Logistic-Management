from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Delivery
from .forms import StartDeliveryForm,AssignDeleveryForm
from payment.models import Payment
from django.conf import settings
from users.models import User
# Create your views here.

def start_delivery(request):
    if request.method == 'POST':
      form = StartDeliveryForm(request.POST)
      if form.is_valid():
         var=form.save(commit=False)
         var.sender = request.user
         var.save()
         request.session['delivery'] = var.pk
         pk = settings.PAYSTACK_PUBLIC_KEY
         amount = 3000
         payment = Payment.objects.create(amount=amount , email=request.user.email, user=request.user)
         payment.save()
         context = {
          'payment':payment,
          'paystack_public_key':pk,
          'amount_value':payment.amount_value(),
          'amount':amount,
          'var':var,
         }
         
         return render(request, 'make_payment.html', context)
      else:
         messages.warning(request, 'Somthing Error')
         return redirect('start_delivery')
    else:
      form =StartDeliveryForm()
      context={
        "form":form
      }
      return render(request,'start_delivery.html' ,context )
         

def active_delivery(request):
   obj = Delivery.objects.filter(sender=request.user, is_verified=True)
   context={'obj':obj}
   return render (request,"active_delivery.html",context)


def assign_delivery(request,pk):
   obj = Delivery.objects.get(pk=pk)
   if request.method == 'POST':
      form = AssignDeleveryForm(request.POST, instance=obj)
      if form.is_valid():
        var = form.save(commit=False)
        var.has_rider = True
        var.save()
        messages.success(request, f'{var.rider} assign to deliver the pakage')
        return redirect('delivery_queue')
      else:
        messages.warning(request, 'Somthing went Error')
        return redirect('delivery_queue')
   else:
      form =AssignDeleveryForm(instance=obj)
      form.fields['rider'].queryset = User.objects.filter(rider=True)
      context = {
         "form":form,
         "obj":obj,
      }
      return render(request ,'assign_delevery.html',context)


def delivery_queue(request):
   obj = Delivery.objects.filter(is_verified=True).order_by('-data_created')
   context={'obj':obj}
   return render (request,"delivery_queue.html",context)


def rider_queue(request):
   obj = Delivery.objects.filter(rider=request.user, is_verified=True)
   context={"obj" : obj}
   return render (request ,"rider_queue.html",context)


def complete_delivery(request,pk):
   obj = Delivery.objects.get(pk=pk)
   obj.is_delivered=True
   obj.save()
   messages.success(request, 'Package Deliverd')
   return redirect('rider_queue')

# def rider_delivery_history(request):
#    obj = Delivery.objects.filter(rider=request.user, is_verified=True)
#    context={"obj" : obj}
#    return render (request ,"rider_delivery_history.html",context)