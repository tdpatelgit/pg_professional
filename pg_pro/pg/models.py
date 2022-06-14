from typing import Optional, Iterable
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets


VEHICLE_TYPE = {
    ('2 Wheeler', '2 Wheeler'),
    ('4 Wheeler', '4 Wheeler')
}

class Vehicle(models.Model):
    type = models.CharField(max_length=20, choices=VEHICLE_TYPE, default='2 Wheeler')
    model_name = models.CharField(max_length=50, null=False, blank=False)
    manufacturer = models.CharField(max_length=50, null=False, blank=False)
    number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.type} :: {self.number} [{self.model_name} - {self.manufacturer}]'


class Guest(models.Model):
    full_name = models.CharField(max_length=200)
    mobile_number = models.DecimalField(max_digits=12, decimal_places=0)
    non_refundable_amount = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    refundable_amount = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    rental = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    purpose = models.CharField(max_length=50, null=True)
    work_place = models.CharField(max_length=50, null=True)
    first_arrival_date = models.DateTimeField(auto_now=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.full_name} (+{self.mobile_number})'


# Serializers define the API representation.
class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ['url', 'full_name', 'mobile_number', 'rental']

# ViewSets define the view behavior.
class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


IDENTITY_TYPE = {
    ('Aadhar Card', 'Aadhar Card'),
    ('Driving License', 'Driving License')
}

class Identity(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    identify_type = models.CharField(max_length=20, choices=IDENTITY_TYPE, default='Aadhar Card')
    identity_proof = models.FileField(upload_to='static/data/guest/identity/', null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.guest.full_name} -> {self.identify_type} size: {len(self.identity_proof)}'


PAYMENT_CHOICES = (
    ('Cash', 'Cash'),
    ('GPay', 'GPay'),
    ('PhonePe', 'PhonePe'),
    ('UPI', 'UPI')
)

class Payment(models.Model):
    date = models.DateTimeField(auto_created=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    source_account_name = models.CharField(max_length=200)
    source_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='Cash')
    destination_account_name = models.CharField(max_length=200)
    destination_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='Cash')
    remarks = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f'{self.date} Rs. {self.amount} {self.source_account_name} to {self.destination_account_name}'

STAY_TYPE = (
    ('Daily', 'Daily'),
    ('Monthly', 'Monthly')
)

ACCOMODATION_TYPE = (
    ('Single', 'Single'),
    ('Double', 'Double'),
    ('Triple', 'Triple')
)

class Stay(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    stay_type = models.CharField(max_length=20, choices=STAY_TYPE, default='Monthly')
    accomodation_type = models.CharField(max_length=20, choices=ACCOMODATION_TYPE, default='Single')
    from_date = models.DateField(auto_created=True)
    to_date = models.DateField(auto_created=True)
    actual_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    payments = models.ManyToManyField(Payment)

    def __str__(self) -> str:
        return f'{self.guest} => {self.from_date} - {self.to_date} :: Rs. {self.amount_paid}'


class Deposite(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    refundable = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    payments = models.ManyToManyField(Payment)

    def __str__(self) -> str:
        return f'{self.guest.full_name} :: Rs. {self.amount} (Refundable Rs. {self.refundable})'


VENDOR_TYPE = (
    ('Online', 'Online'),
    ('Nearby Shop', 'Nearby Shop'),
    ('Market Shop', 'Market Shop'),
    ('Individual', 'Individual'),
    ('Others', 'Others')
)

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=VENDOR_TYPE, default='Individual')
    desciption = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.name} :: {self.type}'

EXPENSE_TYPE = (
    ('House Keeping', 'House Keeping'),
    ('Room Accessory', 'Room Accessory'),
    ('PG Accessory', 'PG Accessory'),
    ('Eletricity', 'Eletricity'),
    ('Plumbing', 'Plumbing'),
    ('Others', 'Others')
)

EXPENSE_FREQUENCY = (
    ('Recurring', 'Recurring'),
    ('One Time', 'One Time')
)

class Expense(models.Model):
    type = models.CharField(max_length=20, choices=EXPENSE_TYPE, default='House Keeping')
    frequency = models.CharField(max_length=20, choices=EXPENSE_FREQUENCY, default='Recurring')
    date = models.DateField(auto_created=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='Cash')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f'{self.date} :: {self.title} ({self.type}) Rs. {self.amount}'
