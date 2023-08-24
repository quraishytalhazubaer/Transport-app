from django.contrib import admin
from .models import *

# Registering models here.

admin.site.register(Measurement)
admin.site.register(Rider)
admin.site.register(Contact)
admin.site.register(Conv)

admin.site.register(Air)
admin.site.register(Bus)
admin.site.register(Launch)
admin.site.register(Train)
admin.site.register(Car)
admin.site.register(Bike)
admin.site.register(CNG)
admin.site.register(Microbus)

admin.site.register(Air_Book)
admin.site.register(Bus_Book)
admin.site.register(Launch_Book)
admin.site.register(Train_Book)
