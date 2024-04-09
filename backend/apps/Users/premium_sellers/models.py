from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from apps.cars_details.cars.models import CarModel


class PremiumSellerModel(BaseModel):
    class Meta:
        db_table = 'premium_seller'
        ordering = ('id',)

    cars = models.ManyToManyField(CarModel, related_name="premium_sellers")
    premium_seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="premium_sellers")


# class AdvertisementModel(BaseModel):
#     view_count = models.PositiveIntegerField(default=0)
    # cars
