from django.contrib import admin
from .models import Guest, Identity, Payment, Stay, Deposite, Vendor, Expense

admin.site.register(Guest)
admin.site.register(Payment)
admin.site.register(Stay)
admin.site.register(Deposite)
admin.site.register(Vendor)
admin.site.register(Expense)
admin.site.register(Identity)