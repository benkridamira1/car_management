import datetime
from django.db import models

# This s the car model.
class Car(models.Model):
    car_title=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.IntegerField()
    condition=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField(max_length=500)
    car_photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    body_style=models.CharField(max_length=100)
    engine=models.CharField(max_length=100)
    transmission=models.CharField(max_length=100)
    interior=models.CharField(max_length=100)
    miles=models.IntegerField()
    doors=models.IntegerField()
    passengers=models.IntegerField()
    milage=models.IntegerField()
    fuel_type=models.CharField(max_length=100)
    is_featured=models.BooleanField(default=False )
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.car_title