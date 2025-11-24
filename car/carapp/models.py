from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand = models.CharField(max_length=10)
    car_name = models.CharField(max_length=10)
    engineum = models.IntegerField()
    release = models.DateField()

class CarAdmin(admin.ModelAdmin):
    list_display=('brand','car_name','engineum','release')

