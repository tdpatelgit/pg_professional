from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Guest, Payment, Stay, Vendor, Expense


# @login_required(login_url='/login/')
def website_home(request):
    template = loader.get_template('website/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

# @login_required(login_url='/login/')
def website_amenities(request):
    template = loader.get_template('website/amenities.html')
    context = {}
    return HttpResponse(template.render(context, request))

# @login_required(login_url='/login/')
def website_packages(request):
    template = loader.get_template('website/packages.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def guest_index(request):
    latest_guest_list = Guest.objects.order_by('-full_name')[:5]
    template = loader.get_template('guest/index.html')
    context = {
        'latest_guest_list': latest_guest_list,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def guest_add(request):
    template = loader.get_template('guest/add.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def guest_detail(request, guest_id):
    try:
        guest = Guest.objects.get(pk=guest_id)
        stays = Stay.objects.filter(guest=guest)
    except Guest.DoesNotExist:
        raise Http404("Guest does not exist")
    return render(request, 'guest/detail.html', {'guest': guest, 'stays': stays})


@login_required(login_url='/login/')
def payment_index(request):
    latest_payment_list = Payment.objects.order_by('-date')[:5]
    template = loader.get_template('payment/index.html')
    context = {
        'latest_payment_list': latest_payment_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def payment_detail(request, payment_id):
    try:
        payment = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        raise Http404("Payment does not exist")
    return render(request, 'payment/detail.html', {'payment': payment})


@login_required(login_url='/login/')
def stay_index(request):
    latest_stay_list = Stay.objects.order_by('-from_date')[:5]
    template = loader.get_template('stay/index.html')
    context = {
        'latest_stay_list': latest_stay_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def stay_detail(request, stay_id):
    try:
        stay = Stay.objects.get(pk=stay_id)
    except Stay.DoesNotExist:
        raise Http404("Stay does not exist")
    return render(request, 'stay/detail.html', {'stay': stay})


@login_required(login_url='/login/')
def vendor_index(request):
    latest_vendor_list = Vendor.objects.order_by('-name')
    template = loader.get_template('vendor/index.html')
    context = {
        'latest_vendor_list': latest_vendor_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def vendor_detail(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        raise Http404("vendor does not exist")
    return render(request, 'vendor/detail.html', {'vendor': vendor})


@login_required(login_url='/login/')
def expense_index(request):
    latest_expense_list = Expense.objects.order_by('-date')[:5]
    template = loader.get_template('expense/index.html')
    context = {
        'latest_expense_list': latest_expense_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def expense_detail(request, expense_id):
    try:
        expense = Expense.objects.get(pk=expense_id)
    except Expense.DoesNotExist:
        raise Http404("expense does not exist")
    return render(request, 'expense/detail.html', {'expense': expense})


@login_required(login_url='/login/')
def user_detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'user/detail.html', {'user': user})
