from django.urls import include, path
from django.contrib.auth import views as auth_views
from .models import Guest

from . import views
from . import models
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'guests', models.GuestViewSet)


urlpatterns = [
    path('api/', include(router.urls)),

    # /pg/home
    path('', views.website_home, name='website_home'),
    path('home/', views.website_home, name='website_home'),

    # login / logout
    path('login/', auth_views.LoginView.as_view(template_name='website/login.html'), name='website_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='website/home.html'), name='website_logout'),

    # /pg/amenities
    path('amenities/', views.website_amenities, name='website_amenities'),

    # /pg/packages
    path('packages/', views.website_packages, name='website_packages'),

    # /pg/user/<id>
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),

    # /pg/guest
    path('guest/', views.guest_index, name='guest_index'),

    # /pg/guest/add
    path('guest/add', views.guest_add, name='guest_add'),

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
