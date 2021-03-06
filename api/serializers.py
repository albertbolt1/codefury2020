from rest_framework import serializers 
from api.models import OrderUser,Order,District,Tailor,TailorWorkAllocated,DistrictwiseReadyList,Valet
class DistrictSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = District
        fields = ('id','url','name')


class OrderUserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = OrderUser
        fields = ('id','url','name','phonenumber','houseno','city','district','email','password')



class OrderSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Order
        fields = ('id','url','ordergiver','gloves_small','gloves','sweater_small','sweater','socks','muffler','monkey_cap_small','monkey_cap','order_processed')




class TailorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tailor
        fields = ('id','url','firstname','lastname','phonenumber','password','working_cap_perday','houseno','city','district','work_allocated')



class TailorWorkAllocatedSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = TailorWorkAllocated
        fields = ('id','url','tailor','gloves_small','gloves','sweater_small','sweater','socks','muffler','monkey_cap_small','monkey_cap','order_completed','dateofallocation','picked_up_or_not')




class DistrictwiseReadyListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = DistrictwiseReadyList
        fields = ('id','url','district','gloves_small','gloves','sweater_small','sweater','socks','muffler','monkey_cap_small','monkey_cap')


class ValetSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Valet
        fields = ('id','url','name','password','vehicleno','phonenumber','city','district','driverbusy_or_not')



