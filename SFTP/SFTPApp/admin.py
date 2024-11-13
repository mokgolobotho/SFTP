from django.contrib import admin
from .models import File, EasyDumps

# Register your models here.
admin.site.register(File)
@admin.register(EasyDumps)
class EasyDumpsAdmin(admin.ModelAdmin):
    list_display = ("id", "terminal_id", "time", "amount", "transaction_fee", "easy_ref", "date", "payment_type", "paid_amount", "bank_cost", "sof_info" ,"created_on") 