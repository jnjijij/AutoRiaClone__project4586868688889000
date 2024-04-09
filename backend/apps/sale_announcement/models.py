from django.db import models

from core.models import BaseModel

from ..cars_details.cars.models import CarModel
from .status_choices import StatusChoices


class SaleAnnouncementModel(BaseModel):
    class Meta:
        db_table = 'sale_announcement'
        ordering = ('id',)

    status = models.CharField(max_length=20, choices=StatusChoices.choices),
    cars = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='sale_announcement')
    attempts = models.IntegerField(default=0)