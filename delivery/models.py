from django.db import models
from users.models import User
# Create your models here.

class Delivery(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    pickup_address = models.CharField(max_length=100)
    recipinet_name = models.CharField(max_length=100)
    recipinet_phone = models.CharField(max_length=50)
    recipinet_address = models.CharField(max_length=50)
    rider = models.ForeignKey(User ,on_delete=models.CASCADE, related_name='delivery_rider', null=True,blank=True)
    is_delivered = models.BooleanField(default=False)
    data_created = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    has_rider = models.BooleanField(default=False)

    def __str__(self):
      return self.package_name
    
    
