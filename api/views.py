from django.shortcuts import render
from datetime import datetime
# Create your views here.
from rest_framework import viewsets
from rest_framework import status
from api.models import OrderUser,Order,District,Tailor,TailorWorkAllocated,DistrictwiseReadyList,Valet
from api.serializers import OrderUserSerializer,OrderSerializer,DistrictSerializer,TailorSerializer,TailorWorkAllocatedSerializer,DistrictwiseReadyListSerializer,ValetSerializer
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

class DistrictwiseReadyListSerializerView(viewsets.ModelViewSet):
	queryset = DistrictwiseReadyList.objects.all()
	serializer_class=DistrictwiseReadyListSerializer

class ValetView(viewsets.ModelViewSet):
	queryset = Valet.objects.all()
	serializer_class=ValetSerializer



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
			beta=requests.put(url,json=req_json)
			print(beta.json())
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
				if(sum(c[i])>0):
					url="http://127.0.0.1:8000/TailorworkAllocated/"
					today_date=datetime.today().strftime('%Y-%m-%d')
					myobj={'tailor':b[i]['id'],'gloves_small':c[i][0],'gloves':c[i][1],'sweater_small': c[i][2],'sweater': c[i][3],'socks': c[i][4],'muffler': c[i][5],'monkey_cap_small':c[i][6],'monkey_cap': c[i][7],"dateofallocation":today_date}
					x=requests.post(url,json=myobj)
					urlmobile = "https://http-api.d7networks.com/send"
					mobileno=b[i]['phonenumber']
					mobileno="+91"+mobileno

					custommessage="Hey "+str(b[i]['firstname'])+" "+str(b[i]['lastname'])+" you have been allocated with gloves small:"+str(c[i][0])+" gloves:"+str(c[i][1])+" sweater small:"+str(c[i][2])+" sweater:"+str(c[i][3])+" socks:"+str(c[i][4])+" muffler:"+str(c[i][5])+" monkeycap small:"+str(c[i][6])+" monkey cap:"+str(c[i][7])+" Thank you, call +917829826952 for further queries"
					querystring = {
					"username":"bhpq4660",
					"password":"mBTcsbRf",
					"from":"Test%20SMS",
					"content":custommessage,
					"dlr-method":"POST",
					"dlr-url":"https://4ba60af1.ngrok.io/receive",
					"dlr":"yes",
					"dlr-level":"3",
					"to":mobileno
					}
					headers = {
					'cache-control': "no-cache"
					}
					response = requests.request("GET", urlmobile, headers=headers, params=querystring)
					print(response)

			for i in a1:
				url="http://127.0.0.1:8000/order/"+str(i['id'])+"/"
				x=requests.get(url)
				req_json=x.json()
				del req_json['url'];
				del req_json['id'];
				req_json['order_processed']=True
				beta=requests.put(url,json=req_json)

			j=0
			for i in b:

				if(sum(c[j])>0):
					url="http://127.0.0.1:8000/Tailor/"+str(i['id'])+"/"
					x=requests.get(url)
					req_json=x.json()
					del req_json['url'];
					del req_json['id'];
					req_json['work_allocated']=True
					betaq=requests.put(url,json=req_json)
					j+=1
				




			return JsonResponse({'message':'allocation was successfull'})




@api_view(['GET'])
def donewithallocatedproducts(request,pk):
	if(request.method=="GET"):
		url="http://127.0.0.1:8000/TailorworkAllocated/"+str(pk)+"/"
		x=requests.get(url)
		req_json=x.json()
		completed_or_not=req_json['order_completed']
		if(completed_or_not==False):
			tailor_id=req_json['tailor']
			tailorobject=Tailor.objects.get(pk=tailor_id)
			tailorobject=tailorobject.__dict__
			districtid=tailorobject['district_id']
			urlputfornow="http://127.0.0.1:8000/TailorworkAllocated/"+str(pk)+"/"
			x=requests.get(url)
			req_jsonfornow=x.json()
			del req_jsonfornow['id']
			del req_jsonfornow['url']
			req_jsonfornow['order_completed']=True
			betaq=requests.put(urlputfornow,json=req_jsonfornow)
			print(betaq.json())

			urlfordist="http://127.0.0.1:8000/DistrictwiseReadyList/"
			xy=requests.get(urlfordist)
			req_json_list=xy.json()
			req_json_list=req_json_list[0]

			noof_gloves_small=req_json['gloves_small']+req_json_list['gloves_small']
	
			noof_gloves=req_json['gloves']+req_json_list['gloves']
			noof_sweater_small=req_json['sweater_small']+req_json_list['sweater_small']
			noof_sweater=req_json['sweater']+req_json_list['sweater']
			noof_socks=req_json['socks']+req_json_list['socks']
			noof_muffler=req_json['muffler']+req_json_list['muffler']
			noof_monkey_cap_small=req_json['monkey_cap_small']+req_json_list['monkey_cap_small']
			noof_monkey_cap=req_json['monkey_cap']+req_json_list['monkey_cap']
			myobj={'district':districtid,'gloves_small':noof_gloves_small,'gloves':noof_gloves,'sweater_small':noof_sweater_small,'sweater':noof_sweater,'socks':noof_socks,'muffler':noof_muffler,'monkey_cap_small':noof_monkey_cap_small,'monkey_cap':noof_monkey_cap}
			urlforput="http://127.0.0.1:8000/DistrictwiseReadyList/"+str(districtid)+"/"
			xy=requests.put(urlforput,json=myobj)
			return JsonResponse({'message':"work done"})

		else:
			return JsonResponse({'message':"already completed"})



@api_view(['GET'])
def districtwisesendtopeople(request,pk):
	if(request.method=="GET"):
		url="http://127.0.0.1:8000/DistrictwiseReadyList/"+str(pk)+"/"
		x=requests.get(url)
		a=x.json()
		noof_gloves_small=a["gloves_small"]
		noof_gloves=a["gloves"]
		noof_sweater_small=a["sweater_small"]
		noof_sweater=a["sweater"]
		noof_socks=a["socks"]
		noof_muffler=a["muffler"]
		noof_monkey_cap_small=a["monkey_cap_small"]
		noof_monkey_cap=a["monkey_cap"]
		#print(noof_gloves_small,noof_gloves,noof_sweater_small,noof_sweater,noof_socks,noof_muffler,noof_monkey_cap_small,noof_monkey_cap)
		allpendingorders=Order.objects.filter(ordergiver__district__id=pk)

		pendingorders=[]
		for i in allpendingorders:
			pendingorders.append(i.__dict__)

		#print(pendingorders)


		completed=[]
		for i in range(len(pendingorders)):
			tnoof_gloves_small=pendingorders[i]["gloves_small"]
			tnoof_gloves=pendingorders[i]["gloves"]
			tnoof_sweater_small=pendingorders[i]["sweater_small"]
			tnoof_sweater=pendingorders[i]["sweater"]
			tnoof_socks=pendingorders[i]["socks"]
			tnoof_muffler=pendingorders[i]["muffler"]
			tnoof_monkey_cap_small=pendingorders[i]["monkey_cap_small"]
			tnoof_monkey_cap=pendingorders[i]["monkey_cap"]
			#print(tnoof_gloves_small,tnoof_gloves,tnoof_sweater_small,tnoof_sweater,tnoof_socks,tnoof_muffler,tnoof_monkey_cap_small,tnoof_monkey_cap)
			if(tnoof_gloves_small<=noof_gloves_small and tnoof_gloves<=noof_gloves and tnoof_sweater_small<=noof_sweater_small and tnoof_sweater<=noof_sweater and tnoof_socks<=noof_socks and tnoof_muffler<=noof_muffler and tnoof_monkey_cap_small<=noof_monkey_cap_small and tnoof_monkey_cap<=noof_monkey_cap):
				completed.append(pendingorders[i]['id'])
				#print(tnoof_gloves_small,tnoof_gloves,tnoof_sweater_small,tnoof_sweater,tnoof_socks,tnoof_muffler,tnoof_monkey_cap_small,tnoof_monkey_cap)
				noof_gloves_small-=tnoof_gloves_small
				noof_gloves-=tnoof_gloves
				noof_sweater_small-=tnoof_sweater_small
				noof_sweater-=tnoof_sweater
				noof_socks-=tnoof_socks
				noof_muffler-=tnoof_muffler
				noof_monkey_cap_small-=tnoof_monkey_cap_small
				noof_monkey_cap-=tnoof_monkey_cap

		print(noof_gloves_small,noof_gloves,noof_sweater_small,noof_sweater,noof_socks,noof_muffler,noof_monkey_cap_small,noof_monkey_cap)
		urld="http://127.0.0.1:8000/DistrictwiseReadyList/"+str(pk)+"/"
		myobj={"district":pk,"gloves_small":noof_gloves_small,"gloves":noof_gloves,"sweater_small": noof_sweater_small,"sweater": noof_sweater,"socks": noof_socks,"muffler": noof_muffler,"monkey_cap_small": noof_monkey_cap_small,"monkey_cap": noof_monkey_cap}
		xdput=requests.put(urld,json=myobj)
		print(xdput.json())
		print(completed)
		for i in completed:
			urllast="http://127.0.0.1:8000/order/"+str(i)+"/"
			x1=requests.get(urllast)
			a12=x1.json()
			ordergiver=a12['ordergiver']
			data=OrderUser.objects.get(pk=ordergiver)
			data=data.__dict__
			mobileno=data['phonenumber']
			print(mobileno)
			urlmobile = "https://http-api.d7networks.com/send"
			mobileno="+91"+mobileno

			custommessage="your order is completed and it will be delivered to you soon, Thank you , for any queries contact +917829826952"
			querystring = {
			"username":"bhpq4660",
			"password":"mBTcsbRf",
			"from":"Test%20SMS",
			"content":custommessage,
			"dlr-method":"POST",
			"dlr-url":"https://4ba60af1.ngrok.io/receive",
			"dlr":"yes",
			"dlr-level":"3",
			"to":mobileno
			}
			headers = {
			'cache-control': "no-cache"
			}
			response = requests.request("GET", urlmobile, headers=headers, params=querystring)
		return JsonResponse({'message':'successfull'})
	




@api_view(['GET'])
def autoservice(request,slug):
	notdeliveredlist=TailorWorkAllocated.objects.filter(tailor__district__name=slug,picked_up_or_not=False,order_completed=True).order_by('dateofallocation').reverse()
	driverlist=Valet.objects.filter(district__name=slug,driverbusy_or_not=False)
	a=[]
	b=[]
	for i in notdeliveredlist:
		a.append(i.__dict__)
	for j in driverlist:
		b.append(j.__dict__)

	if(len(a)<=0 or len(b)<=0):
		return JsonResponse({'message':'NO orders available'})
	else:
		object1=Valet.objects.get(id=b[0]['id'])
		name=object1.name
		object1.driverbusy_or_not=True
		object1.save()
		object2=TailorWorkAllocated.objects.get(id=a[0]['id'])
		object2.picked_up_or_not=True
		object2.save()
		address=str(object2.tailor.houseno)+" "+str(object2.tailor.city)


		phonenumber=b[0]['phonenumber']

		urlmobile = "https://http-api.d7networks.com/send"
		mobileno="+91"+phonenumber
		custommessage="please pick the parcels from "+ address +" and take it to depo"
		querystring = {
		"username":"bhpq4660",
		"password":"mBTcsbRf",
		"from":"Test%20SMS",
		"content":custommessage,
		"dlr-method":"POST",
		"dlr-url":"https://4ba60af1.ngrok.io/receive",
		"dlr":"yes",
		"dlr-level":"3",
		"to":mobileno
		}
		headers = {
		'cache-control': "no-cache"
		}
		response = requests.request("GET", urlmobile, headers=headers, params=querystring)

		return JsonResponse({name:address})

