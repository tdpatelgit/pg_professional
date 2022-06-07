from django.urls import path

from . import views

urlpatterns = [
    # /pg/home
    path('home/', views.website_home, name='website_home'),

    # /pg/amenities
    path('amenities/', views.website_amenities, name='website_amenities'),

    # /pg/packages
    path('packages/', views.website_packages, name='website_packages'),

    # /pg/guest
    path('guest/', views.guest_index, name='guest_index'),

    # /pg/guest/<id>
    path('guest/<int:guest_id>/', views.guest_detail, name='guest_detail'),

    # /pg/payment
    path('payment/', views.payment_index, name='payment_index'),

    # /pg/payment/<id>
    path('payment/<int:payment_id>/', views.payment_detail, name='payment_detail'),

    # /pg/stay
    path('stay/', views.stay_index, name='stay_index'),

    # /pg/stay/<id>
    path('stay/<int:stay_id>/', views.stay_detail, name='stay_detail'),

    # /pg/vendor
    path('vendor/', views.vendor_index, name='vendor_index'),

    # /pg/vendor/<id>
    path('vendor/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),

    # /pg/expense
    path('expense/', views.expense_index, name='expense_index'),

    # /pg/expense/<id>
    path('expense/<int:expense_id>/', views.expense_detail, name='expense_detail'),
]
