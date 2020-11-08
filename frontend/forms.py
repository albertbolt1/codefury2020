from django.forms import ModelForm
from api.models import OrderUser,Order,District,Tailor,Valet
from django import forms



class OrderUserForm(ModelForm):

	class Meta:
		model=OrderUser
		fields = ['name','phonenumber','houseno','city','district','email','password' ]



class OrderForm(ModelForm):

	class Meta:
		model=Order
		fields = ['ordergiver','gloves_small','gloves','sweater_small','sweater','socks','muffler','monkey_cap_small','monkey_cap']



class TailorForm(ModelForm):

	class Meta:
		model=Tailor
		fields = ['firstname','lastname','phonenumber','password','working_cap_perday','houseno','city','district']



class UserLoginForm(forms.Form):
	name = forms.CharField(max_length=10)
	phonenumber = forms.CharField(max_length=10)
	password = forms.CharField(max_length=100)


class ValetForm(forms.Form):
	class Meta:
		model=Valet
		fields = ['name','password','vehicleno','phonenumber','city','district']




   