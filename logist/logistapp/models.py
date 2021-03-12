from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.
Location= [
    ('delhi', 'Delhi'),
    ('bangalore', 'Bangalore'),
    ('chennai', 'Chennai'),
    ]
Truck=[
('flatbed Truck', 'Flatbed Truck'),
('garbage Truck', 'Garbage Truck'),
('dump Truck', 'Dump Truck'),
]

class Trip(models.Model):
    trip_name=models.CharField(max_length=200, )
    source= models.CharField(max_length=200, choices=Location)
    destination = models.CharField(max_length=200, choices=Location)
    truck_type= models.CharField(max_length=200, choices=Truck)
    Date_time = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("trip_detail",kwargs={'pk':self.pk})

    def ___str__(self):
        return self.trip_name



# class TripForm(ModelForm):
#     class Meta:
#         model=Trip
#         fields=['source','destination','truck_type']
