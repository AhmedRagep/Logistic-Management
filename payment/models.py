from django.db import models
from users.models import User
import secrets
from .paystack import Paystack
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        # يستمر في التغير الي ان يتم جلب قيمه
        while not self.ref:
            # انشاء قيمة عشوائيه واضافتها في المتغير بطول 50 حرف
            ref = secrets.token_urlsafe(50)
            # البحث عن القيمه في عنصر المودل اذا كانت موجوده
            similar_ref = Payment.objects.filter(ref=ref)
            # اذا لم تكن موجوده
            if not similar_ref:
                # يتم حفظها في عنصر المودل
                self.ref = ref
        super().save(*args, **kwargs)

    # ضرب قيمة الدفع في 100
    def amount_value(self):
        return int(self.amount) * 100

    def verify_payment(self):
        # اضافة التحقق في هذا المتغير
        paystack = Paystack()
        # الدخول الي التحقق واضافه متغيرين من المودل
        status, result = paystack.verify_payment(self.ref,self.amount)
        # لو تم التحقق
        if status:
            # لو الرقم مقسوم علي 100 يساوي قيمه الرقم في المودل
            if result['amount']/100 == self.amount:
              # اجعل قيمه الفريفاي بمفعل
              self.verified = True
              # احفظ
              self.save()
              print("Payment Verified")
              # لو تم التفعيل ارجع القيمه مفعله
            if self.verified:
                return True
            # لو القيمه غير مفعله ارجع ذالك
            else :
                return False
              