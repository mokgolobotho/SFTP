from django.db import models

# Create your models here.
class EasyDumps(models.Model):
    terminal_id = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=120)
    amount = models.FloatField()
    transaction_fee = models.FloatField()
    easy_ref = models.CharField(max_length=20)
    date = models.DateField()
    payment_type = models.CharField(max_length=100, null=True, blank=True)
    paid_amount = models.FloatField()
    bank_cost = models.FloatField()
    sof_info = models.CharField(max_length=300,)
    created_on = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    file = models.FileField(upload_to= "files")