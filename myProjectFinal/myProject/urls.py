from unicodedata import name
from django.contrib import admin
from django.urls import path
from transport.views import *
from pdf_convert.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('about',about, name='about'),
    path('online',online,name='online'),
    path('adminpage',adminpage,name='adminpage'),
    path('addroute',addroute,name='addroute'),
    path("availableroutes",availableroutes,name='availableroutes'),
    path("offer",offer,name='offer'),
    path("contact",contact,name='contact'),
    path("comment",comment,name='comment'),
    path("profile",profilepage,name='profilepage'),
    path("payment",payment,name='payment'),
    path('abc',abc,name='abc'),
    path('signup', handleSignUp, name="handleSignUp"),
    path('login', handeLogin, name="handleLogin"),
    path('logout', handelLogout, name="handleLogout"),
    path('forgotpass', forgetPassword, name="forgetpass"),
    path('changepass', changePassword, name="changepass"),
    path('measurement',calc_dist_view, name="calculate-view"),
    path('bcash',bcash,name='bcash'),
    path('nagad',nagad,name='nagad'),
    path('cellfin',cellfin,name='cellfin'),
    path('searchresult',searchresult,name='searchresult'),
    path('chat/', chat, name='chat'),
    path('webhook/', webhook, name='webhook'),

    
    path('air',air,name='air'),
    path("update_airstatus/<str:pk>/",updateairstatus,name='updateairstatus'),
    path('findair', findair, name="findair"),
    path('airbookings', airbookings, name="airbookings"),
    path('aircancellings', aircancellings, name="aircancellings"),
    path('seeairbookings', seeairbookings, name="seeairbookings"),
    path('showairtickets',show_air,name='showairtickets'),
    path('printairPDF',pdf_air,name='printairPDF'),


    path('bus',bus,name='bus'),
    path("update_busstatus/<str:pk>/",updatebusstatus,name='updatebusstatus'),
    path('findbus', findbus, name="findbus"),
    path('busbookings', busbookings, name="busbookings"),
    path('buscancellings', buscancellings, name="buscancellings"),
    path('seebusbookings', seebusbookings, name="seebusbookings"),
    path('showbustickets',show_bus,name='showbustickets'),
    path('printbusPDF',pdf_bus,name='printbusPDF'),


    path('launch',launch,name='launch'),
    path("update_launchstatus/<str:pk>/",updatelaunchstatus,name='updatelaunchstatus'),
    path('findlaunch', findlaunch, name="findlaunch"),
    path('launchbookings', launchbookings, name="launchbookings"),
    path('launchcancellings', launchcancellings, name="launchcancellings"),
    path('seelaunchbookings', seelaunchbookings, name="seelaunchbookings"),
    path('showlaunchtickets',show_launch,name='showlaunchtickets'),
    path('printlaunchPDF',pdf_launch,name='printlaunchPDF'),


    path('train',train,name='train'),
    path("update_trainstatus/<str:pk>/",updatetrainstatus,name='updatetrainstatus'),
    path('findtrain', findtrain, name="findtrain"),
    path('trainbookings', trainbookings, name="trainbookings"),
    path('traincancellings', traincancellings, name="traincancellings"),
    path('seetrainbookings', seetrainbookings, name="seetrainbookings"),
    path('showtraintickets',show_train,name='showtraintickets'),
    path('printtrainPDF',pdf_train,name='printtrainPDF'),



    path('car',car,name='car'),
    path("update_carstatus/<str:pk>/",updatecarstatus,name='updatecarstatus'),
    path('seecarhistory',seecarhistory,name='seecarhistory'),
    path('showcartickets',show_car,name='showcartickets'),
    path('printcarPDF',pdf_car,name='printcarPDF'),

    path('bike',bike,name='bike'),
    path("update_bikestatus/<str:pk>/",updatebikestatus,name='updatebikestatus'),
    path('seebikehistory',seebikehistory,name='seebikehistory'),
    path('showbiketickets',show_bike,name='showbiketickets'),
    path('printbikePDF',pdf_bike,name='printbikePDF'),

    path('CNG',cng,name='CNG'),
    path("update_cngstatus/<str:pk>/",updatecngstatus,name='updatecngstatus'),
    path('seecnghistory',seecarhistory,name='seecnghistory'),
    path('showcngtickets',show_cng,name='showcngtickets'),
    path('printcngPDF',pdf_cng,name='printcngPDF'),

    path('microbus',microbus,name='microbus'),
    path("update_microstatus/<str:pk>/",updatemicrostatus,name='updatemicrostatus'),
    path('seemicrohistory',seecarhistory,name='seemicrohistory'),
    path('showmicrotickets',show_micro,name='showmicrotickets'),
    path('printmicroPDF',pdf_micro,name='printmicroPDF'),


    path("delete_comment/<str:pk>/",deleteComments,name='deleteComments'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
