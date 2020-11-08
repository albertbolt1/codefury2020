from django.shortcuts import render
from django.shortcuts import redirect
from api.models import OrderUser,Order,District,Tailor
# Create your views here.
from frontend.forms import OrderUserForm,OrderForm,TailorForm,UserLoginForm,ValetForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def ordergiver(request):
	form=OrderUserForm()
	return render(request,'frontend/ordergiver.html',{'form':form})

@login_required
def order(request):
	if not request.user.is_authenticated:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	form=OrderForm()
	return render(request,'frontend/order.html',{'form':form})


def tailor(request):
	form=TailorForm()
	return render(request,'frontend/tailor.html',{'form':form})


def ordergiverpost(request):
	if request.method == 'POST':
		form= OrderUserForm(request.POST)

		if form.is_valid():
			form.save()

		data = request.POST
		name=data['name']
		email=data['email']
		password=data['password']



		user = User.objects.create_user(name,email,password)

		return redirect('login/')



def tailorpost(request):
	if request.method == 'POST':
		form= TailorForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,"frontend/tailorlogin.html")


def autowala(request):
	form=ValetForm()
	print(form)
	return render(request,"frontend/autowala.html",{'form':form})



def orderpost(request):
	if request.method == 'POST':
		form= OrderForm(request.POST)
		if form.is_valid():
			form.save()
		data=request.POST
		gloves_small=data['gloves_small']
		gloves=data['gloves']
		sweater_small=data['sweater_small']
		sweater=data['sweater']
		socks=data['socks']
		muffler=data['muffler']
		monkey_cap_small=data['monkey_cap_small']
		monkey_cap=data['monkey_cap']
		str1="Yor order of "+"gloves small:"+str(gloves_small)+" gloves:"+str(gloves)+" sweater small:"+str(sweater_small)+" sweater:"+str(sweater)+" socks:"+str(socks)+" muffler:"+str(muffler)+" monkeycap small:"+str(monkey_cap_small)+" monkey cap:"+str(monkey_cap)+" has been placed,Thank you, call +917829826952 for further queries"

		return render(request,'frontend/done.html',{'str1':str1})

def home(request):
	return render(request,'frontend/home.html')


