from django.db import models

from core.models import BaseModel

from apps.cars_details.cars.models import CarModel


class CarViewModel(BaseModel):
    class Meta:
        db_table = 'car_views'

    car_ad = models.OneToOneField(CarModel, on_delete=models.CASCADE, related_name='car_views')
    views = models.IntegerField(default=0)

