from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from api.models import OrderUser,Order,District,Tailor,TailorWorkAllocated
from api.serializers import OrderUserSerializer,OrderSerializer,DistrictSerializer,TailorSerializer,TailorWorkAllocatedSerializer
from rest_framework.decorators import api_view
from django.core import serializers
from django.http.response import JsonResponse
import requests 
import math

class DistrictView(viewsets.ModelViewSet):
	queryset = District.objects.all()
	serializer_class=DistrictSerializer

class OrderUserView(viewsets.ModelViewSet):
	queryset = OrderUser.objects.all()
	serializer_class=OrderUserSerializer



class OrderView(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class=OrderSerializer


class TailorView(viewsets.ModelViewSet):
	queryset = Tailor.objects.all()
	serializer_class=TailorSerializer


class TailorWorkAllocatedView(viewsets.ModelViewSet):
	queryset = TailorWorkAllocated.objects.all()
	serializer_class=TailorWorkAllocatedSerializer


@api_view(['GET'])
def district_wise_results(request,slug):
	try:
		orderlist=Order.objects.filter(ordergiver__district__name=slug,order_processed=False)
	except:
		return JsonResponse({'message': 'The pizza does not exist'}, status=status.HTTP_404_NOT_FOUND)
	if(request.method=="GET"):
		noof_gloves_small=0
		noof_gloves=0
		noof_sweater_small=0
		noof_sweater=0
		noof_socks=0
		noof_muffler=0
		noof_monkey_cap_small=0
		noof_monkey_cap=0
		for i in range(0,len(orderlist)):
			data=orderlist[i].__dict__
			noof_gloves_small+=data['gloves_small']
			noof_gloves+=data['gloves']
			noof_sweater_small+=data['sweater_small']
			noof_sweater+=data['sweater']
			noof_socks+=data['socks']
			noof_muffler+=data['muffler']
			noof_monkey_cap_small+=data['monkey_cap_small']
			noof_monkey_cap+=data['monkey_cap']
		data={'noof_gloves_small':noof_gloves_small,'noof_gloves':noof_gloves,'noof_sweater_small':noof_sweater_small,'noof_sweater':noof_sweater,'noof_socks':noof_socks,'noof_muffler':noof_muffler,'noof_monkey_cap_small':noof_monkey_cap_small,'noof_monkey_cap':noof_monkey_cap}
		return JsonResponse(data,safe=False)


@api_view(['GET'])
def district_wise_results(request,slug):
	try:
		orderlist=Order.objects.filter(ordergiver__district__name=slug,order_processed=False)
	except:
		return JsonResponse({'message': 'The pizza does not exist'}, status=status.HTTP_404_NOT_FOUND)
	if(request.method=="GET"):
		noof_gloves_small=0
		noof_gloves=0
		noof_sweater_small=0
		noof_sweater=0
		noof_socks=0
		noof_muffler=0
		noof_monkey_cap_small=0
		noof_monkey_cap=0
		for i in range(0,len(orderlist)):
			data=orderlist[i].__dict__
			noof_gloves_small+=data['gloves_small']
			noof_gloves+=data['gloves']
			noof_sweater_small+=data['sweater_small']
			noof_sweater+=data['sweater']
			noof_socks+=data['socks']
			noof_muffler+=data['muffler']
			noof_monkey_cap_small+=data['monkey_cap_small']
			noof_monkey_cap+=data['monkey_cap']
		data={'noof_gloves_small':noof_gloves_small,'noof_gloves':noof_gloves,'noof_sweater_small':noof_sweater_small,'noof_sweater':noof_sweater,'noof_socks':noof_socks,'noof_muffler':noof_muffler,'noof_monkey_cap_small':noof_monkey_cap_small,'noof_monkey_cap':noof_monkey_cap}
		return JsonResponse(data,safe=False)

@api_view(['GET'])
def allocatedistrict(request,slug):
	orderlist=Order.objects.filter(ordergiver__district__name=slug,order_processed=False).order_by('sweater')
	a1=[]
	"""tailorlist=Tailor.objects.filter(work_allocated=False).order_by('working_cap_perday').reverse()
	a=[]
	b=[]
	"""

	for i in orderlist:
		a1.append(i.__dict__)
	print(a1)
	"""
	for i in tailorlist:
		b.append(i.__dict__)"""

	url1="http://127.0.0.1:8000/api/district/"+str(slug)
	a=requests.get(url1)
	a=a.json()
	print(a)
	tailorlist=Tailor.objects.filter(work_allocated=False).order_by('working_cap_perday')
	b=[]
	for i in tailorlist:
		b.append(i.__dict__)
	length=len(b)
	print(b)
	noof_gloves_small=a["noof_gloves_small"]
	noof_gloves=a["noof_gloves"]
	noof_sweater_small=a["noof_sweater_small"]
	noof_sweater=a["noof_sweater"]
	noof_socks=a["noof_socks"]
	noof_muffler=a["noof_muffler"]
	noof_monkey_cap_small=a["noof_monkey_cap_small"]
	noof_monkey_cap=a["noof_monkey_cap"]
	k1=noof_gloves_small//length
	k2=noof_gloves//length
	k3=noof_sweater_small//length
	k4=noof_sweater//length
	k5=noof_socks//length
	k6=noof_muffler//length
	k7=noof_monkey_cap_small//length
	k8=noof_monkey_cap//length
	c=[]
	if(length==1):
		c.append([noof_gloves_small,noof_gloves,noof_sweater_small,noof_sweater,noof_socks,noof_muffler,noof_monkey_cap_small,noof_monkey_cap])
		url="http://127.0.0.1:8000/TailorworkAllocated/"
		myobj={'tailor':b[0]['id'],'gloves_small':noof_gloves_small,'gloves':noof_gloves,'sweater_small': noof_sweater_small,'sweater': noof_sweater,'socks': noof_socks,'muffler': noof_muffler,'monkey_cap_small':noof_monkey_cap_small,'monkey_cap': noof_monkey_cap}
		x=requests.post(url,json=myobj)

		for i in a1:
			url="http://127.0.0.1:8000/order/"+str(i['id'])+"/"
			x=requests.get(url)
			req_json=x.json()
			del req_json['url'];
			del req_json['id'];
			req_json['order_processed']=True
			b=requests.put(url,json=req_json)
			print(b.json())
	else:
		array=[noof_gloves_small,noof_gloves,noof_sweater_small,noof_sweater,noof_socks,noof_muffler,noof_monkey_cap_small,noof_monkey_cap]
		if(array.count(0)==len(array)):
			return JsonResponse({'message':'no resource to allocate'})
		else:
			c=[[] for i in range(length)]
			for k1 in array:
				z=math.ceil(k1/length)
				for i in range(length):
					if(k1>=z):
						c[i].append(z)
						k1-=z
					elif(k1<z and k1>0):
						c[i].append(k1)
						k1=0
					elif(k1==0):
						c[i].append(0)

			for i in range(length):
				url="http://127.0.0.1:8000/TailorworkAllocated/"
				myobj={'tailor':b[i]['id'],'gloves_small':c[i][0],'gloves':c[i][1],'sweater_small': c[i][2],'sweater': c[i][3],'socks': c[i][4],'muffler': c[i][5],'monkey_cap_small':c[i][6],'monkey_cap': c[i][7]}
				x=requests.post(url,json=myobj)

			for i in a1:
				url="http://127.0.0.1:8000/order/"+str(i['id'])+"/"
				x=requests.get(url)
				req_json=x.json()
				del req_json['url'];
				del req_json['id'];
				req_json['order_processed']=True
				b=requests.put(url,json=req_json)

			return JsonResponse({'message':'allocation was successfull'})














