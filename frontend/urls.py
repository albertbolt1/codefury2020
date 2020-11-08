
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^login/$', auth_views.LoginView.as_view(template_name="frontend/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="frontend/logout.html"), name='logout'),
    path('ordergiver',views.ordergiver,name="giveorder"),
    path('order',views.order,name="order"),
    path('tailor',views.tailor,name="tailor"),
    path('ordergiverpost',views.ordergiverpost,name="ordergiverpost"),
    path('tailorpost',views.tailorpost,name="tailorpost"),
    path('orderpost',views.orderpost,name="orderpost"),
    path('autowala',views.autowala,name="auto"),
    path('home',views.home,name="home"),
]
