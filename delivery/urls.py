from django.urls import path
from .views import start_delivery,active_delivery,assign_delivery,delivery_queue,rider_queue,complete_delivery

urlpatterns = [
    path('start_delivery', start_delivery, name='start_delivery'),
    path('active_delivery', active_delivery, name='active_delivery'),
    path('delivery_queue', delivery_queue, name='delivery_queue'),
    path('assign_delivery/<int:pk>', assign_delivery, name='assign_delivery'),
    path('rider_queue', rider_queue, name='rider_queue'),
    path('complete_delivery/<int:pk>', complete_delivery, name='complete_delivery'),
]
