
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
urlpatterns = [
    path('',include(router.urls)),
    url(r'^api/district/(?P<slug>[-\w]+)$',views.district_wise_results),
    url(r'^api/allocate/(?P<slug>[-\w]+)$',views.allocatedistrict)
]
