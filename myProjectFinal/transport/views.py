from datetime import date, datetime

from calendar import HTMLCalendar
from decimal import Decimal
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .helper import send_forget_password_mail

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,get_object_or_404
import folium
import geocoder
from transport.decoretor import allowed_users

from geopy.geocoders import Nominatim
from geopy import distance
from geopy.distance import geodesic

from transport.form import AirStatusForm, BikeStatusForm, BusStatusForm, CarStatusForm, CngStatusForm, LaunchStatusForm, MicroStatusForm, RiderForm,MeasurementModelForm, TrainStatusForm
from transport.models import *

from django.db.models import Q

from django.http import JsonResponse
import json
import requests

def numOfDays(date1, date2):
    return (date2-date1).days

def homepage(request):
    return render(request,'index.html')

def about (request):
    now = datetime.now()
    context = {'posting_time': now}
    return render(request,'aboutpage.html',context)
    

def online(request):
    return render(request,'TermsAndConditions.html')

def abc(request):
    return HttpResponse('Hello Bhai')

def addroute(request):
    return render(request,'addroute.html')


def handleSignUp(request):
          if request.method=="POST":
               # Get the post parameters
               username=request.POST['username']
               fname=request.POST['fname']
               lname=request.POST['lname']
               email=request.POST['email']
               pass1=request.POST['pass1']
               pass2=request.POST['pass2']

               # check for errorneous input
               if len(username)<5:
                    messages.error(request, " Your user name must be under 5 characters")
                    return redirect('homepage')

               if not username.isalnum():
                    messages.error(request, " User name should only contain letters and numbers")
                    return redirect('/')
               if (pass1!= pass2):
                    messages.error(request, " Passwords do not match, try again please")
                    return redirect('/')
               
               # Create the user
               if User.objects.filter(username=username).first():
                         messages.error(request, "This username is already taken, try another for example: username123")
                         return redirect('/')

               myuser = User.objects.create_user(username,email,pass1)
               myuser.first_name= fname
               myuser.last_name= lname
               myuser.save()

               g = Group.objects.get(name='Rider')
               users = User.objects.filter(username=username)
               for u in users:
                g.user_set.add(u)

                Rider.objects.create(
				user=myuser,
				name=myuser.username,
                fname=myuser.first_name,
                lname=myuser.last_name,
				email=myuser.email,
				)

               messages.success(request, " Your account has been successfully created")
               return redirect('/')
        
          else:
               return HttpResponse("404 - Not found")

def handeLogin(request):
        if request.method=="POST":
            # Get the post parameters
            loginusername=request.POST['loginusername']
            loginpassword=request.POST['loginpassword']

            user=authenticate(username= loginusername, password= loginpassword)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return render(request, 'index.html')
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("/")
        else:
            messages.error(request, "Please login to get to the page")
            return render(request, 'index.html')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')


def changePassword(request):
    context = {}
    username = request.POST.get('username')
    try:
        profile_obj = Rider.objects.filter(username=username).first()
        user_id = profile_obj.user.id
        # context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            return redirect('http://127.0.0.1:8000/admin/auth/user/{user_id}/password/')         
            
        # user_obj = User.objects.get(id = user_id)
        # user_obj.set_password(new_password)
        # user_obj.save()
        # return redirect('/login/')


    except Exception as e:
        print(e)
    return render (request, 'changepass.html')

def forgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            history = request.POST.get('history')
            dateused = request.POST.get('dateused')

            if not User.objects.filter(username=username).first():
                messages.error(request, "No user found with this username")
                return redirect("homepage")

            # user_obj = User.objects.get(username=username)
            resetpass = Resetpass(username=username,phone=phone,email=email,history=history,dateused=dateused)
            resetpass.save()
            messages.success(request, 'Your reset password request has been sent, you will get an email soon')
            return redirect("homepage")

    except Exception as e:
        print(e)
    return render(request,'forgetPass.html')


def profilepage(request):
     rider =request.user.rider
     form = RiderForm(instance=rider)

     if request.method== 'POST':
          form=RiderForm(request.POST, request.FILES, instance=rider)
          if form.is_valid():
               form.save()
               messages.success(request, "Profile data has been updated")
     context ={'form':form}
     return render(request,"profile.html",context)

@login_required(login_url='handleLogin')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact= Contact(name=name,phone=phone,email=email,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent, Thanks for filling out the form!')

    m = folium.Map(location=[23.7778, 90.4057], zoom_start=12)
    folium.Marker([23.765529,90.354312], tooltip='ATMS', popup="Talha's place").add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request,"support.html",context)

def deleteComments(request, pk):
        comment = Contact.objects.get(id=pk) 
        if request.method == "POST":
            comment.delete()
            return redirect('/adminpage')

        context = {'comment':comment}
        return render(request, 'delete.html', context)

def comment(request):
    c = Contact.objects.all()
    context = {'c': c}  
    return render (request,'comment.html',context)


def searchresult (request):
    if 'query' in request.GET:
        q = request.GET['query']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(From__icontains=q) | Q(To__icontains=q))
        data1 = Air.objects.filter(multiple_q)
        data2 = Bus.objects.filter(multiple_q)
        data3 = Launch.objects.filter(multiple_q)
        data4 = Train.objects.filter(multiple_q)
    else:
        messages.success(request, 'Your information is successfully generated')
        return redirect ('home')
    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4
    }
    return render (request, 'index.html',context)

@login_required(login_url='handleLogin')
@allowed_users(allowed_roles=['admin'])
def adminpage(request):
    pay= Pay.objects.all()
    ai = Air_Book.objects.all()
    bu = Bus_Book.objects.all()
    la = Launch_Book.objects.all()
    t = Train_Book.objects.all()
    ca = Car.objects.all()
    bi = Bike.objects.all()
    cn = CNG.objects.all()
    m = Microbus.objects.all()
    
    context = {
        'pay':pay,'ca':ca ,'bi':bi,'cn':cn,'m':m, 'ai':ai,'bu':bu,'la':la,'t':t
    }
    return render(request,"adminpage.html", context)

@login_required(login_url='handleLogin')
def payment(request):
    return render(request, 'payment.html')

@login_required(login_url='handleLogin')
def bcash (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        transection = request.POST.get('transection')
        vehicle = request.POST.get('vehicle')
        datesent = request.POST.get('dateused')

        bkash = Pay(username=username,phone=phone,transection=transection,vehicle=vehicle,datesent=datesent,pmethod='Bkash')
        bkash.save()
        messages.success(request, 'Your information is successfully generated')
        return render (request,'index.html')
    return render (request,'bcash.html')

def nagad (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        transection = request.POST.get('transection')
        vehicle = request.POST.get('vehicle')
        datesent = request.POST.get('dateused')

        bkash = Pay(username=username,phone=phone,transection=transection,vehicle=vehicle,datesent=datesent,pmethod='Nagad')
        bkash.save()
        messages.success(request, 'Your information is successfully generated') 
        return render (request,'index.html')
    return render (request,'nagad.html')

def cellfin (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        transection = request.POST.get('transection')
        vehicle = request.POST.get('vehicle')
        datesent = request.POST.get('dateused')

        bkash = Pay(username=username,phone=phone,transection=transection,vehicle=vehicle,datesent=datesent,pmethod='CellFin')
        bkash.save()
        messages.success(request, 'Your information is successfully generated')
        return render (request,'index.html')
    return render (request,'cellFin.html')

def offer(request):
    return render(request, 'offers.html')

@login_required(login_url='handleLogin')
def availableroutes(request):
    a = Air.objects.all()
    bu = Bus.objects.all()
    la = Launch.objects.all()
    t = Train.objects.all()
    context = {'a': a, 'bu':bu,'la':la,'t':t}  
    return render(request,"availableroutes.html", context)

def calc_dist_view(request):
    # i = get_object_or_404(Measurement, id=i)
    obj = Measurement.objects.all().last()
    forms = MeasurementModelForm(request.POST or None)

    if forms.is_valid():
        instance = forms.save(commit= False)
        instance.location = forms.cleaned_data.get('location')
        instance.destination = forms.cleaned_data.get('destination')
        instance.distance = 500.00
        instance.save()

    context= {
        'distance': obj,
        'form': forms,
    }
    return render(request, 'distance.html',context)



@login_required(login_url='handleLogin')
@allowed_users(allowed_roles=['admin'])
def air(request):
    if request.method=="POST":
        From=request.POST.get('From')
        To=request.POST.get('To')
        air_name = request.POST.get('air_name')
        nos = request.POST.get('nos')
        price = request.POST.get('price')
        type = request.POST.get('type')
        date=request.POST.get('date')
        time=request.POST.get('time')
        
        air = Air(From=From, To=To,date=date,time=time, air_name=air_name, nos= nos, price=price, rem=nos, Class=type)
        air.save()
        messages.success(request, 'Your information is successfully generated')
    return render(request,'air.html')

@login_required(login_url='handleLogin')
def findair(request):
    context = {}
    if request.method == 'POST':
        From = request.POST.get('From')
        To = request.POST.get('To')
        date_r = request.POST.get('date')
        air_list = Air.objects.filter(From=From, To=To, date=date_r)
        if air_list:
            return render(request, 'airlist.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            messages.success(request,"Sorry no buses availiable")
            return render(request, 'findair.html', context)
    else:
        return render(request, 'findair.html')

@login_required(login_url='handleLogin')
def airbookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('air_id')
        seats_r = int(request.POST.get('no_seats'))
        air = Air.objects.get(id=id_r)
        if air:
            if air.rem >= int(seats_r) and seats_r>0:
                name_r = air.air_name
                cost = int(seats_r) * air.price
                From = air.From
                To = air.To
                nos_r = Decimal(air.nos)
                type = air.Class
                price_r = air.price
                date_r = air.date
                time_r = air.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = air.rem - seats_r
                Air.objects.filter(id=id_r).update(rem = rem_r)
                book = Air_Book.objects.create(name=username_r, email=email_r, userid=userid_r, air_name=name_r,
                                           From=From, airid=id_r,
                                           To=To, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'airbookings.html', locals())
            else:
                messages.success(request, "Sorry select fewer number of seats")
                # return redirect('bookings')
                return render(request, 'findair.html', context)
    else:
        return render(request, 'findair.html')

@login_required(login_url='handleLogin')
def aircancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('air_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Air_Book.objects.get(id=id_r)
            air = Air.objects.get(id=book.airid)
            rem_r = air.rem + book.nos
            Air.objects.filter(id=book.airid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Air_Book.objects.filter(id=id_r).update(status='CANCELLED')
            Air_Book.objects.filter(id=id_r).update(nos=0)
            messages.success(request,"Your flight has been cancelled successfully")
            return redirect(seeairbookings)
        except Air_Book.DoesNotExist:
            messages.success(request, "Sorry You have not booked the selected flight")
            return render(request, 'error.html', context)
    else:
        return render(request, 'findair.html')

@login_required(login_url='handleLogin')
def seeairbookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Air_Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'airbookinglist.html', locals())
    else:
        messages.success(request, "Sorry no buses booked")
        return render(request, 'findair.html', context)

@login_required(login_url='handleLogin')
def updateairstatus(request, pk):

	order = Air_Book.objects.get(id=pk)
	form = AirStatusForm(instance=order)

	if request.method == 'POST':
		form = AirStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)

@login_required(login_url='handleLogin')
@allowed_users(allowed_roles=['admin'])
def bus(request):
    if request.method=="POST":
        From=request.POST.get('From')
        To=request.POST.get('To')
        bus_name = request.POST.get('bus_name')
        nos = request.POST.get('nos')
        price = request.POST.get('price')
        type = request.POST.get('type')
        date=request.POST.get('date')
        time=request.POST.get('time')

        bus = Bus(From=From, To=To,date=date,time=time, bus_name=bus_name, nos= nos, price=price, rem=nos, Class=type)
        bus.save()
        messages.success(request, 'Your information is successfully generated')
    return render(request,'bus.html')

@login_required(login_url='handleLogin')
def launch(request):
    if request.method=="POST":
        From=request.POST.get('From')
        To=request.POST.get('To')
        launch_name = request.POST.get('launch_name')
        nos = request.POST.get('nos')
        price = request.POST.get('price')
        type = request.POST.get('type')
        date=request.POST.get('date')
        time=request.POST.get('time')

        launch = Launch(From=From, To=To,date=date,time=time, launch_name=launch_name, nos= nos, price=price, rem=nos, Class=type) 
        launch.save()
        messages.success(request, 'Your information is successfully generated')
    return render(request,'launch.html')

@login_required(login_url='handleLogin')
def train(request):
    if request.method=="POST":
        From=request.POST.get('From')
        To=request.POST.get('To')
        train_name = request.POST.get('train_name')
        nos = request.POST.get('nos')
        price = request.POST.get('price')
        type = request.POST.get('type')
        date=request.POST.get('date')
        time=request.POST.get('time')

        train = Train(From=From, To=To,date=date,time=time, train_name=train_name, nos= nos, price=price, rem=nos, Class=type)
        train.save()
        messages.success(request, 'Your information is successfully generated')
    return render(request,'train.html')

@login_required(login_url='handleLogin')
def car(request):
    From = str(request.POST.get('From'))
    To = str(request.POST.get('To'))
    # date = request.POST.get('date')
    # time = request.POST.get('time')
    date = datetime.now().date() 
    time= datetime.now().time() 

    username_r = request.user.username
    email_r = request.user.email
    userid_r = request.user.id

    start=geocoder.osm(From)
    lat1=start.lat
    lng1=start.lng

    end=geocoder.osm(To)
    lat2=end.lat
    lng2=end.lng

    
    lati=(lat1+lat2)/2
    lngi=(lng1+lng2)/2


    pickup = (lat1,lng1)
    dropoff= (lat2,lng2)

    dist=round(geodesic(pickup,dropoff).km,2)
    fare = round((dist * 15),2)

    if dist<=100:
        zoom =10
    elif dist>100 and dist<=5000:
        zoom=6
    else:
        zoom=4

    if request.method=="POST":
        car = Car(name=username_r, email=email_r, userid=userid_r,From=From, To=To,date=date,time=time,price=fare,status='REQUESTED',paymentstatus='UNPAID')
        car.save()
        tickets = Car.objects.all().last()
        messages.success(request, 'Your information is successfully generated')
        #create map
        m = folium.Map(location=[lati,lngi], zoom_start=zoom)
        folium.Marker([lat1, lng1], tooltip='Pick-up', popup=From).add_to(m)
        folium.Marker([lat2, lng2], tooltip='destination', popup=To).add_to(m)
        folium.PolyLine((pickup,dropoff)).add_to(m)

        m = m._repr_html_()
        context = {
            'm': m,
            'username': username_r,
            'distance': dist,
            'fare': fare,
            'tickets':tickets
        }
        return render(request, 'requested.html',context)
    return render(request,'car.html')

@login_required(login_url='handleLogin')
def updatecarstatus(request, pk):

	order = Car.objects.get(id=pk)
	form = CarStatusForm(instance=order)

	if request.method == 'POST':
		form = CarStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)


@login_required(login_url='handleLogin')
def seecarhistory(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Car.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'carhistory.html', locals())
    else:
        messages.success(request, "Sorry no buses booked")
        return render(request, 'car.html', context)



@login_required(login_url='handleLogin')
def bike(request):
    From = str(request.POST.get('From'))
    To = str(request.POST.get('To'))
    # date = request.POST.get('date')
    # time = request.POST.get('time')
    date = datetime.now().date() 
    time= datetime.now().time() 

    username_r = request.user.username
    email_r = request.user.email
    userid_r = request.user.id

    start=geocoder.osm(From)
    lat1=start.lat
    lng1=start.lng

    end=geocoder.osm(To)
    lat2=end.lat
    lng2=end.lng

    
    lati=(lat1+lat2)/2
    lngi=(lng1+lng2)/2


    pickup = (lat1,lng1)
    dropoff= (lat2,lng2)

    dist=round(geodesic(pickup,dropoff).km,2)
    fare = round((dist * 5),2)

    if dist<=100:
        zoom =10
    elif dist>100 and dist<=5000:
        zoom=6
    else:
        zoom=4

    if request.method=="POST":
        bike = Bike(name=username_r, email=email_r, userid=userid_r,From=From, To=To,date=date,time=time,price=fare,status='REQUESTED',paymentstatus='UNPAID')
        bike.save()
        tickets = Bike.objects.all().last()        
        messages.success(request, 'Your information is successfully generated')
        #create map
        m = folium.Map(location=[lati,lngi], zoom_start=zoom)
        folium.Marker([lat1, lng1], tooltip='Pick-up', popup=From).add_to(m)
        folium.Marker([lat2, lng2], tooltip='destination', popup=To).add_to(m)
        folium.PolyLine((pickup,dropoff)).add_to(m)

        m = m._repr_html_()
        context = {
            'm': m,
            'username': username_r,
            'distance': dist,
            'fare': fare,
            'tickets':tickets
        }
        return render(request, 'requested.html',context)
    return render(request,'bike.html')


@login_required(login_url='handleLogin')
def updatebikestatus(request, pk):

	order = Bike.objects.get(id=pk)
	form = BikeStatusForm(instance=order)

	if request.method == 'POST':
		form = BikeStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)



@login_required(login_url='handleLogin')
def seebikehistory(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Bike.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'bikehistory.html', locals())
    else:
        messages.success(request, "Sorry no buses booked")
        return render(request, 'Bike.html', context)


@login_required(login_url='handleLogin')
def cng(request):
    From = str(request.POST.get('From'))
    To = str(request.POST.get('To'))
    # date = request.POST.get('date')
    # time = request.POST.get('time')
    date = datetime.now().date() 
    time= datetime.now().time() 

    username_r = request.user.username
    email_r = request.user.email
    userid_r = request.user.id

    start=geocoder.osm(From)
    lat1=start.lat
    lng1=start.lng

    end=geocoder.osm(To)
    lat2=end.lat
    lng2=end.lng

    
    lati=(lat1+lat2)/2
    lngi=(lng1+lng2)/2


    pickup = (lat1,lng1)
    dropoff= (lat2,lng2)

    dist=round(geodesic(pickup,dropoff).km,2)
    fare = round((dist * 7),2)

    if dist<=100:
        zoom =10
    elif dist>100 and dist<=5000:
        zoom=6
    else:
        zoom=4

    if request.method=="POST":
        cng = CNG(name=username_r, email=email_r, userid=userid_r,From=From, To=To,date=date,time=time,price=fare,status='REQUESTED',paymentstatus='UNPAID')
        cng.save()
        tickets = CNG.objects.all().last()
        messages.success(request, 'Your information is successfully generated')
        #create map
        m = folium.Map(location=[lati,lngi], zoom_start=zoom)
        folium.Marker([lat1, lng1], tooltip='Pick-up', popup=From).add_to(m)
        folium.Marker([lat2, lng2], tooltip='destination', popup=To).add_to(m)
        folium.PolyLine((pickup,dropoff)).add_to(m)

        m = m._repr_html_()
        context = {
            'm': m,
            'username': username_r,
            'distance': dist,
            'fare': fare,
            'tickets':tickets
        }
        return render(request, 'requested.html',context)
    return render(request,'CNG.html')

@login_required(login_url='handleLogin')
def updatecngstatus(request, pk):

	order = CNG.objects.get(id=pk)
	form = CngStatusForm(instance=order)

	if request.method == 'POST':
		form = CngStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)



@login_required(login_url='handleLogin')
def seecnghistory(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = CNG.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'cnghistory.html', locals())
    else:
        messages.success(request, "Sorry no buses booked")
        return render(request, 'CNG.html', context)

@login_required(login_url='handleLogin')
def microbus(request):
    From = str(request.POST.get('From'))
    To = str(request.POST.get('To'))
    date = request.POST.get('date')
    time = request.POST.get('time')

    username_r = request.user.username
    email_r = request.user.email
    userid_r = request.user.id

    start=geocoder.osm(From)
    lat1=start.lat
    lng1=start.lng

    end=geocoder.osm(To)
    lat2=end.lat
    lng2=end.lng

    
    lati=(lat1+lat2)/2
    lngi=(lng1+lng2)/2


    pickup = (lat1,lng1)
    dropoff= (lat2,lng2)

    dist=round(geodesic(pickup,dropoff).km,2)
    fare = round((dist * 11),2)

    if dist<=100:
        zoom =10
    elif dist>100 and dist<=5000:
        zoom=6
    else:
        zoom=4

    if request.method=="POST":
        microbus = Microbus(name=username_r, email=email_r, userid=userid_r, From=From, To=To,date=date,time=time,price=fare,status='REQUESTED',paymentstatus='UNPAID')
        microbus.save()
        tickets = Microbus.objects.all().last()
        messages.success(request, 'Your information is successfully generated')
        #create map
        m = folium.Map(location=[lati,lngi], zoom_start=zoom)
        folium.Marker([lat1, lng1], tooltip='Pick-up', popup=From).add_to(m)
        folium.Marker([lat2, lng2], tooltip='destination', popup=To).add_to(m)
        folium.PolyLine((pickup,dropoff)).add_to(m)

        m = m._repr_html_()
        context = {
            'm': m,
            'username': username_r,
            'distance': dist,
            'fare': fare,
            'tickets':tickets
        }
        return render(request, 'requested.html',context)
    return render(request,'microbus.html')

@login_required(login_url='handleLogin')
def updatemicrostatus(request, pk):

	order = Microbus.objects.get(id=pk)
	form = MicroStatusForm(instance=order)

	if request.method == 'POST':
		form = MicroStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)



@login_required(login_url='handleLogin')
def seemicrohistory(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Microbus.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'microhistory.html', locals())
    else:
        messages.success(request, "Sorry no buses booked")
        return render(request, 'microbus.html', context)


@login_required(login_url='handleLogin')
def findbus(request):
    context = {}
    if request.method == 'POST':
        From = request.POST.get('From')
        To = request.POST.get('To')
        date_r = request.POST.get('date')

        bus_list = Bus.objects.filter(From=From, To=To, date=date_r)
        if bus_list:
            return render(request, 'buslist.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            messages.success(request,"Sorry no buses availiable")
            return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html')

@login_required(login_url='handleLogin')
def busbookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Bus.objects.get(id=id_r)
        if bus:
            if bus.rem >= int(seats_r) and seats_r>0:
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                From = bus.From
                To = bus.To
                nos_r = Decimal(bus.nos)
                type = bus.Class
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Bus_Book.objects.create(name=username_r, email=email_r, userid=userid_r, bus_name=name_r,
                                           From=From, busid=id_r,
                                           To=To, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'busbookings.html', locals())
            else:
                messages.success(request, "Sorry select fewer number of seats")
                # return redirect('bookings')
                return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html')

@login_required(login_url='handleLogin')
def buscancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Bus_Book.objects.get(id=id_r)
            bus = Bus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Bus_Book.objects.filter(id=id_r).update(status='CANCELLED')
            Bus_Book.objects.filter(id=id_r).update(nos=0)
            messages.success(request,"Your ticket has been cancelled successfully")
            return redirect(seebusbookings)
        except Bus_Book.DoesNotExist:
            messages.success(request, "Sorry You have not booked the selected bus")
            return render(request, 'error.html', context)
    else:
        return render(request, 'findbus.html')

@login_required(login_url='handleLogin')
def seebusbookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Bus_Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'busbookinglist.html', locals())
    else:
        messages.success(request, "Sorry no buses booked")
        return render(request, 'findbus.html', context)

@login_required(login_url='handleLogin')
def updatebusstatus(request, pk):

	order = Bus_Book.objects.get(id=pk)
	form = BusStatusForm(instance=order)

	if request.method == 'POST':
		form = BusStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)




@login_required(login_url='handleLogin')
def findlaunch(request):
    context = {}
    if request.method == 'POST':
        From = request.POST.get('From')
        To = request.POST.get('To')
        date_r = request.POST.get('date')
        launch_list = Launch.objects.filter(From=From, To=To, date=date_r)
        if launch_list:
            return render(request, 'launchlist.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            messages.success(request,"Sorry no launches availiable")
            return render(request, 'findlaunch.html', context)
    else:
        return render(request, 'findlaunch.html')

@login_required(login_url='handleLogin')
def launchbookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('launch_id')
        seats_r = int(request.POST.get('no_seats'))
        launch = Launch.objects.get(id=id_r)
        if launch:
            if launch.rem >= int(seats_r) and seats_r>0:
                name_r = launch.launch_name
                cost = int(seats_r) * launch.price
                From = launch.From
                To = launch.To
                nos_r = Decimal(launch.nos)
                type = launch.Class
                price_r = launch.price
                date_r = launch.date
                time_r = launch.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = launch.rem - seats_r
                Launch.objects.filter(id=id_r).update(rem=rem_r)
                book = Launch_Book.objects.create(name=username_r, email=email_r, userid=userid_r, launch_name=name_r,
                                           From=From, launchid=id_r,
                                           To=To, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'launchbookings.html', locals())
            else:
                messages.success(request, "Sorry select fewer number of seats")
                # return redirect('bookings')
                return render(request, 'findlaunch.html', context)
    else:
        return render(request, 'findlaunch.html')

@login_required(login_url='handleLogin')
def launchcancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('launch_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Launch_Book.objects.get(id=id_r)
            bus = Launch.objects.get(id=book.busid)
            rem_r = launch.rem + book.nos
            Launch.objects.filter(id=book.launchid).update(rem=rem_r)
            #nos_r = launch.nos - seats_r
            Launch_Book.objects.filter(id=id_r).update(status='CANCELLED')
            Launch_Book.objects.filter(id=id_r).update(nos=0)
            messages.success(request,"Your ticket has been cancelled successfully")
            return redirect(seelaunchbookings)
        except Launch_Book.DoesNotExist:
            messages.success(request, "Sorry You have not booked the selected Launch")
            return render(request, 'error.html', context)
    else:
        return render(request, 'findlaunch.html')

@login_required(login_url='handleLogin')
def seelaunchbookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Launch_Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'launchbookinglist.html', locals())
    else:
        messages.success(request, "Sorry no Launches booked")
        return render(request, 'findlaunch.html', context)

@login_required(login_url='handleLogin')
def updatelaunchstatus(request, pk):

	order = Launch_Book.objects.get(id=pk)
	form = LaunchStatusForm(instance=order)

	if request.method == 'POST':
		form = LaunchStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)



@login_required(login_url='handleLogin')
def findtrain(request):
    context = {}
    if request.method == 'POST':
        From = request.POST.get('From')
        To = request.POST.get('To')
        date_r = request.POST.get('date')
        train_list = Train.objects.filter(From=From, To=To, date=date_r)
        if train_list:
            return render(request, 'trainlist.html', locals())
        else:
            # context["error"] = "Sorry no trains availiable"
            messages.success(request,"Sorry no trains availiable")
            return render(request, 'findtrain.html', context)
    else:
        return render(request, 'findtrain.html')

@login_required(login_url='handleLogin')
def trainbookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('train_id')
        seats_r = int(request.POST.get('no_seats'))
        train = Train.objects.get(id=id_r)
        if train:
            if train.rem >= int(seats_r) and seats_r>0:
                name_r = train.train_name
                cost = int(seats_r) * train.price
                From = train.From
                To = train.To
                nos_r = Decimal(train.nos)
                type = train.Class
                price_r = train.price
                date_r = train.date
                time_r = train.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = train.rem - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Train_Book.objects.create(name=username_r, email=email_r, userid=userid_r, train_name=name_r,
                                           From=From, trainid=id_r,
                                           To=To, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'trainbookings.html', locals())
            else:
                messages.success(request, "Sorry select fewer number of seats")
                # return redirect('bookings')
                return render(request, 'findtrain.html', context)
    else:
        return render(request, 'findtrain.html')

@login_required(login_url='handleLogin')
def traincancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('train_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Train_Book.objects.get(id=id_r)
            bus = Train.objects.get(id=book.trainid)
            rem_r = train.rem + book.nos
            Train.objects.filter(id=book.trainid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Train_Book.objects.filter(id=id_r).update(status='CANCELLED')
            Train_Book.objects.filter(id=id_r).update(nos=0)
            messages.success(request,"Your ticket has been cancelled successfully")
            return redirect(seetrainbookings)
        except Train_Book.DoesNotExist:
            messages.success(request, "Sorry You have not booked the selected bus")
            return render(request, 'error.html', context)
    else:
        return render(request, 'findtrain.html')

@login_required(login_url='handleLogin')
def seetrainbookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Train_Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'trainbookinglist.html', locals())
    else:
        messages.success(request, "Sorry no trains booked")
        return render(request, 'findtrain.html', context)

@login_required(login_url='handleLogin')
def updatetrainstatus(request, pk):

	order = Train_Book.objects.get(id=pk)
	form = TrainStatusForm(instance=order)

	if request.method == 'POST':
		form = TrainStatusForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('adminpage')

	context = {'form':form}
	return render(request, 'update.html', context)


@login_required(login_url='handleLogin')
@csrf_exempt
def chat(request):    
    if request.method == 'POST':
        user = request.user.rider
        user_message = request.POST.get('message')  # Assuming the user's message is sent as 'message'
        print(user_message)
        # Send the user message to your Node.js application
        node_url = 'http://localhost:3001/bot'  # Replace with your Node.js application's URL
        response = requests.post(node_url, json={'message': user_message})
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            bot_response = data.get('response')  # Get the bot's response from the JSON data
                
            conversation = Conv(user=user, user_message = user_message,response=bot_response)
            conversation.save()

            c = Conv.objects.all()
            print(c)
            #'user':user, 'user_message': user_message, 'bot_response':bot_response
            context = {'c':c}
            return render (request,'chat.html',context)


            # Render chat.html template with user_message and bot_response
            #return render(request, 'chat.html', {'user_message': user_message, 'bot_response': bot_response})
        else:
            messages.success(request, "Sorry, Could not reach the server !")
    
    #return JsonResponse({'error': 'Invalid request method'})
    return render(request, 'chat.html')


@csrf_exempt
def webhook(request):
    # Parse the incoming JSON request from Dialogflow
    req = json.loads(request.body)
    #print(req)
    # Get the action from the JSON data
    action = req.get('queryResult').get('action')
    
    if action == 'FindBus':
        departure_location = req.get('queryResult').get('parameters').get('DepartureLocation')
        destination = req.get('queryResult').get('parameters').get('Destination')
        print(departure_location[0])
        print(destination[0])

        # Fetch bus information based on departure location and destination
        bus_info = Bus.objects.filter(From=departure_location[0], To=destination[0])
        if bus_info:
            response_text = []
            #response_text = f"Buses available from {departure_location[0]} to {destination[0]}:\n"
            for bus in bus_info:
                response_text.append(f"{bus.bus_name} {bus.date} {bus.time}\n")
                #response_text += f"- Bus name {bus.bus_name}, Departure: {bus.date}-{bus.time}\n"
            print(response_text[0])
        else:
            response_text = f"No buses found from {departure_location} to {destination}."
    else:
        response_text = "I'm sorry, I didn't quite catch that."
    
    # Construct the Dialogflow webhook response
    fulfillmentText = {
        # 'fulfillmentText': response_text
        "fulfillmentMessages": 
        [
            {
                "text": 
                    {
                        "text": [response_text[0]]          
                    }
            },
                       {
            "card": {
                "title": "Product Details",
                "subtitle": "Product ABC",
                "imageUri": "https://static.busbd.com.bd/busbdmedia/16991652_1397658293641231_1205628201074067845_o.1501711430",
                "buttons": [
                {
                    "text": "Buy Now",
                    "postback": "https://f513-103-85-159-146.ngrok-free.app/"
                },
                {
                    "text": "More Info",
                    "postback": "https://www.hanifenterprise.com/"
                }

                ]
            }
            },
            {
                "text": 
                    {
                        "text": [response_text[1]]          
                    }
            },            
            {
            "card": {
                "title": "Product Details",
                "subtitle": "Product ABC",
                "imageUri": "https://chokrojan-bucket.s3.ap-southeast-1.amazonaws.com/company/slides/he_place_slide_2.jpg",
                "buttons": [
                {
                    "text": "Buy Now",
                    "postback": "https://f513-103-85-159-146.ngrok-free.app/"
                },
                {
                    "text": "More Info",
                    "postback": "https://www.hanifenterprise.com/"
                }

                ]
            }
            }

        ]
    }
    # Return the response
    return JsonResponse(fulfillmentText, safe=False)


def get_orm_object_by_action(request, model_name):
    try:
        # model = apps.get_model(app_label='transport', model_name=model_name)
        if True:
            objects = Bus.objects.all()

            # Convert each model instance to JSON using the utility function
            serialized_objects = [model_to_json(obj) for obj in objects]

            return JsonResponse({'result': 'success', 'data': serialized_objects})
        else:
            return JsonResponse({'result': 'error', 'message': 'Model not found'})
    except Exception as e:
        return JsonResponse({'result': 'error', 'message': str(e)})