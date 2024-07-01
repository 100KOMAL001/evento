from django.db import models
from django.contrib.auth.models import User




# Create your models here.
# forms.py
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField(blank=False)
    def __str__(self):
        return self.name
# models.py



class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    detail=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
    
#class cart(models.Model):
   # uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    #pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    #qty=models.IntegerField(default=1)
    #amt=models.IntegerField()
class Event(models.Model):
    pid=models.ForeignKey('Package',on_delete=models.CASCADE,db_column='pid')
    name = models.CharField(max_length=255,verbose_name='Event name')
    venue = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} at {self.venue} on {self.date} at {self.time}"
class BookingHistory(models.Model):
    uid = models.ForeignKey('auth.User', on_delete=models.CASCADE,db_column='uid')
    pid = models.ForeignKey('Package', on_delete=models.CASCADE,db_column='pid')
    #eid = models.ForeignKey('Event',on_delete=models.CASCADE,db_column='eid')

    def __str__(self):
        return f"Booking by {self.user.username} for {self.event.name}"