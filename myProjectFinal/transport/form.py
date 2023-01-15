from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model= Measurement
        fields = ('location','destination',)
        

class RiderForm(ModelForm):
    class Meta:
        model = Rider
        fields = '__all__'
        exclude = ['user']



class AirStatusForm(forms.ModelForm):
    class Meta:
        model = Air_Book
        fields = ('status','paymentstatus',)

class BusStatusForm(forms.ModelForm):
    class Meta:
        model = Bus_Book
        fields = ('status','paymentstatus',)

class LaunchStatusForm(forms.ModelForm):
    class Meta:
        model = Launch_Book
        fields = ('status','paymentstatus',)

class TrainStatusForm(forms.ModelForm):
    class Meta:
        model = Train_Book
        fields = ('status','paymentstatus',)



class CarStatusForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('status','paymentstatus',)

class BikeStatusForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ('status','paymentstatus',)

class CngStatusForm(forms.ModelForm):
    class Meta:
        model = CNG
        fields = ('status','paymentstatus',)

class MicroStatusForm(forms.ModelForm):
    class Meta:
        model = Microbus
        fields = ('status','paymentstatus',)
