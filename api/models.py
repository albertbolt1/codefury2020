from django.db import models
import datetime
class District(models.Model):
    name= models.CharField(max_length=50,blank=False)
    def __str__(self):
        return "%s" % (self.name)

class OrderUser(models.Model):
    name = models.CharField(max_length=100,blank=False)
    phonenumber=models.CharField(max_length=100,blank=False)
    houseno=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    email= models.CharField(max_length=100,blank=False)
    password = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return "%s %s" % (self.name, self.phonenumber)

class Order(models.Model):
    ordergiver=models.ForeignKey(OrderUser, on_delete=models.CASCADE)
    gloves_small=models.IntegerField()
    gloves=models.IntegerField()
    sweater_small=models.IntegerField()
    sweater=models.IntegerField()
    socks=models.IntegerField()
    muffler=models.IntegerField()
    monkey_cap_small=models.IntegerField()
    monkey_cap=models.IntegerField()
    order_processed=models.BooleanField(default=False)

    def __str__(self):
        return "%s" % (self.ordergiver)



class Tailor(models.Model):
    firstname=models.CharField(max_length=100,blank=False)
    lastname=models.CharField(max_length=100,blank=True)
    phonenumber=models.CharField(max_length=10,blank=False)
    password = models.CharField(max_length=100,blank=False)
    working_cap_perday=models.IntegerField(null=False,default=0)
    houseno=models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    work_allocated=models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.firstname,self.lastname)


class TailorWorkAllocated(models.Model):
    tailor=models.ForeignKey(Tailor, on_delete=models.CASCADE)
    gloves_small=models.IntegerField()
    gloves=models.IntegerField()
    sweater_small=models.IntegerField()
    sweater=models.IntegerField()
    socks=models.IntegerField()
    muffler=models.IntegerField()
    monkey_cap_small=models.IntegerField()
    monkey_cap=models.IntegerField()
    order_completed=models.BooleanField(default=False)
    dateofallocation=models.DateField(default=datetime.date.today)
    picked_up_or_not=models.BooleanField(default=False)

class DistrictwiseReadyList(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    gloves_small=models.IntegerField(default=0)
    gloves=models.IntegerField(default=0)
    sweater_small=models.IntegerField(default=0)
    sweater=models.IntegerField(default=0)
    socks=models.IntegerField(default=0)
    muffler=models.IntegerField(default=0)
    monkey_cap_small=models.IntegerField(default=0)
    monkey_cap=models.IntegerField(default=0)



class Valet(models.Model):
    name=models.CharField(max_length=20, null=False)
    password=models.CharField(max_length=20, null=False)
    vehicleno=models.CharField(max_length=20, null=False)
    phonenumber=models.CharField(max_length=10,blank=False)
    city=models.CharField(max_length=100)
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    driverbusy_or_not=models.BooleanField(default=False)

