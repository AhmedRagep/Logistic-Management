from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Payment
from delivery.models import Delivery
# Create your views here.

def verify_payment(request, ref):
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()

    if verified:
        obj = Delivery.objects.get(pk=request.session['delivery'])
        obj.is_verified = True
        obj.save()
        messages.success(request, 'Payment Verified, Comming Soon')
        return redirect('dashboard')
    else :
        messages.warning(request, 'Somthing Went Error, Please try again')
        return redirect('dashboard')