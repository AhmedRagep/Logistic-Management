from django import forms
from .models import Delivery

class StartDeliveryForm(forms.ModelForm):
    
    class Meta:
        model = Delivery
        fields = ['package_name','pickup_address','recipinet_name','recipinet_phone','recipinet_address']


class AssignDeleveryForm(forms.ModelForm):
    class Meta:
      model=Delivery
      fields = ['rider']
    