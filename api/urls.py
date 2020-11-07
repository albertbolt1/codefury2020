
from django.urls import path,include
from . import views
from rest_framework import routers 
from django.conf.urls import url 
router = routers.DefaultRouter()
router.register('district',views.DistrictView)
router.register('ordergiver',views.OrderUserView)
router.register('order',views.OrderView)
router.register('Tailor',views.TailorView)
router.register('TailorworkAllocated',views.TailorWorkAllocatedView)
router.register('DistrictwiseReadyList',views.DistrictwiseReadyListSerializerView)
urlpatterns = [
    path('',include(router.urls)),
    url(r'^api/district/(?P<slug>[-\w]+)$',views.district_wise_results),
    url(r'^api/allocate/(?P<slug>[-\w]+)$',views.allocatedistrict),
    url(r'^api/orderdone/(?P<pk>[0-9]+)$',views.donewithallocatedproducts),
    url(r'^api/sendtopeople/(?P<pk>[0-9]+)$',views.districtwisesendtopeople)
]
