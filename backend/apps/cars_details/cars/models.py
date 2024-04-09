from datetime import datetime

from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.all_users.users.models import ProfileModel
from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from core.enums.regex_enums import RegexEnum
from core.models import BaseModel

from ..brand_models.models import CarBrandModel, CarsModelModel
from .choices import *
from .managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.ForeignKey(CarBrandModel, on_delete=models.CASCADE, related_name='cars')
    cars_model = models.ForeignKey(CarsModelModel, on_delete=models.CASCADE, related_name='cars')
    # model = models.CharField(max_length=25, validators=(
    #     validators.RegexValidator(RegexEnum.MODEL.pattern, RegexEnum.MODEL.msg),
    # )
    #                          )
    # color = models.CharField(max_length=25
    #                          #                          , validators=(
    #                          #     validators.RegexValidator(RegexEnum.COLOR.pattern, RegexEnum.COLOR.msg)
    #                          # )
    #                          )
    # year = models.IntegerField(validators=(
    #     validators.MinValueValidator(1885),
    #     validators.MaxValueValidator(datetime.now().year)
    # )
    # )
    price = models.IntegerField(validators.MinValueValidator(0), validators=[MaxValueValidator(100000000)])
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices, default='UAH')
    # seat_count = models.IntegerField(default=0)
    # body_type = models.CharField(max_length=11, choices=BodyTypeChoices.choices)
    # engine_type = models.CharField(max_length=25, choices=EngineTypesChoices.choices)
    # engine_volume = models.FloatField(default=0)
    # transmission = models.CharField(max_length=25, choices=TransmissionTypeChoices.choices)
    # mileage = models.IntegerField()
    region = models.CharField(max_length=25)
    premium_seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='premium_seller', null=True)
    seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='seller', null=True)
    # image = models.ImageField()
    # attempts = models.IntegerField(default=0)

    objects = CarManager()

# class CarViewModel(BaseModel):
#     class Meta:
#         db_table = 'car_views'
#
#     car_ad = models.OneToOneField(CarModel, on_delete=models.CASCADE, related_name='car_views')
#     car_views = models.IntegerField(default=0)


# class AdvertisementModel(BaseModel):
#     view_count = models.PositiveIntegerField(default=0)

# def save(self, *args, **kwargs):
#     if self.brand is None:
#         raise ValidationError('Brand is missing contact with manager manager@gmail.com')
#     super(CarModel, self).save(*args, **kwargs)

# def validate_brand(self, data):
#     if data['brand'] :
#         raise ValidationError('Brand is missing contact with manager manager@gmail.com')
#     return data

# def validate_brand(self, brand):
#     if not brand:
#         send_mail(
#             'Brand not available',
#             'The serializer did not receive any data',
#             'from@example.com',  # виправити на email продавця
#             ['manager@example.com'],
#             fail_silently=False,
#         )
#     return brand
