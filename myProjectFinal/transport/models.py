from re import U
from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import  User
# Create your models here.

class Measurement (models.Model):
    location  = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" from {self.location} to {self.destination} is {self.distance} km"

class Rider(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=13,null=True)
    address = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="static/ImageUpload/img200.png", null=True, blank=True)

    def __str__(self):
	    return str(self.name) if self.name else ''


class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name


class Pay(models.Model):
    username = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    transection = models.CharField(max_length=122)
    vehicle = models.CharField(max_length=12)
    pmethod = models.CharField(max_length=12)
    datesent = models.DateField(null=True)
  
    def __str__(self) -> str:
        return self.username

class Resetpass(models.Model):
    username = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    history = models.CharField(max_length=12)
    dateused = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username

class Air(models.Model):
    air_name = models.CharField(max_length=30)
    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    Class = models.CharField(max_length=20)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Air route {self.From} to {self.To}"    

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    Class = models.CharField(max_length=20)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Bus route {self.From} to {self.To}"    

class Launch(models.Model):
    launch_name = models.CharField(max_length=30)
    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    Class = models.CharField(max_length=20)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Launch route {self.From} to {self.To}"  

class Train(models.Model):
    train_name = models.CharField(max_length=30)
    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    Class = models.CharField(max_length=20)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Train route {self.From} to {self.To}"  


class Car(models.Model):
    REQUESTED = 'Requested'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'
    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   
    

    TICKET_STATUSES = ((REQUESTED, 'Requested'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
              
    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(choices=TICKET_STATUSES, default=REQUESTED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)

class Bike(models.Model):
    REQUESTED = 'Requested'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'
    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   
    

    TICKET_STATUSES = ((REQUESTED, 'Requested'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
             
    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(choices=TICKET_STATUSES, default=REQUESTED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)

class CNG(models.Model):
    REQUESTED = 'Requested'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'
    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   
    

    TICKET_STATUSES = ((REQUESTED, 'Requested'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
             
    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(choices=TICKET_STATUSES, default=REQUESTED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)


class Microbus(models.Model):
    REQUESTED = 'Requested'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'
    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   
    

    TICKET_STATUSES = ((REQUESTED, 'Requested'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)
                
    
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)

    From  = models.CharField(max_length=20)
    To = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(choices=TICKET_STATUSES, default=REQUESTED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)

class Air_Book(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'

    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    airid=models.DecimalField(decimal_places=0, max_digits=2)
    air_name = models.CharField(max_length=30)
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)

    def __str__(self):
        return f"Air from {self.From} to {self.To}"


class Bus_Book(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'

    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid = models.DecimalField(decimal_places=0, max_digits=2)
    busid = models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)

    def __str__(self):
        return f"Bus from {self.From} to {self.To}"

class Launch_Book(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'

    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    launchid=models.DecimalField(decimal_places=0, max_digits=2)
    launch_name = models.CharField(max_length=30)
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)

    def __str__(self):
        return f"Launch from {self.From} to {self.To}"

class Train_Book(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'

    PAID = 'Paid'
    UNPAID = 'Unpaid'

    
    PAYMENT_STATUSES = ((PAID, 'Paid'),
                     (UNPAID, 'Unpaid'),)   

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       (COMPLETED, 'Completed'),)
                       
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    trainid=models.DecimalField(decimal_places=0, max_digits=2)
    train_name = models.CharField(max_length=30)
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=11)
    paymentstatus = models.CharField(choices= PAYMENT_STATUSES, default=UNPAID, max_length=11)

    def __str__(self):
        return f"Train from {self.From} to {self.To}"


class Conv(models.Model):
    user = models.ForeignKey(Rider, on_delete=models.CASCADE)
    user_message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.user_message}"
