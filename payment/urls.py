from django.urls import path
from .views import verify_payment

urlpatterns = [
    path('verify-payment/<str:ref>/', verify_payment, name='verify_payment')
]
