from datetime import date, datetime, timedelta

from django.contrib import messages
from django.core.mail import send_mail
from django.db import models, transaction
from django.db.models import Avg, Count, manager
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests

from .models import CarModel


def average_price_in_region(price, region):
    average_price_by_regions = CarModel.objects.filter(region=region).aggregate(avg_price=Avg('price'))
    return average_price_by_regions['avg_price']


def average_price(price):
    average_price = CarModel.objects.aggregate(Avg('price'))
    return average_price['price__avg']


def get_currency_exchange_rates():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    data = response.json()
    exchange_rates = {}
    for currency in data:
        if currency['ccy'] in ['USD', 'EUR']:
            exchange_rates[currency['ccy']] = float(currency['buy'])
    return exchange_rates


def calculate_price_in_currency(price, currencies):
    exchange_rates = get_currency_exchange_rates()
    recalculated_prices = {}
    for currency in currencies:
        recalculated_prices[currency] = price / exchange_rates[currency]
    return recalculated_prices


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = (
            'id', 'brand', 'cars_model', 'price', 'seller', 'currency', 'premium_seller',
            # 'color', 'year', 'seat_count', 'body_type',
            # 'engine_type',
            # 'engine_volume',
            # 'transmission', 'mileage',
            'region',
        )
        read_only_fields = ('seller', 'premium_seller',
                            )

    # def save(self, instance, validated_data):
    #     if self.attempts >= 3:
    #         self.attempts = 0
    #         messages.warning('Ad creation car blocked. Contact manager to unblocked')
    #         return super().save(instance)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        price = data['price']
        recalculated_prices = calculate_price_in_currency(price, ['USD', 'EUR'])
        data['price_usd'] = recalculated_prices['USD']
        data['price_eur'] = recalculated_prices['EUR']
        return data



class PremiumSellersCarsSerializer(CarSerializer):

    class Meta:
        model = CarModel
        fields = (
            'id', 'brand', 'cars_model', 'price', 'seller', 'currency', 'premium_seller', 'region',
            # 'attempts',
        )
        read_only_fields = ('seller', 'premium_seller', 'attempts'
                            # 'car_views',
                            )


    # def save(self, *args, **kwargs):
    #     if self.attempts >= 3:
    #         self.attempts = 0
    #         messages.warning('Ad creation car blocked. Contact manager to unblocked')
    #         return super().save(*args, **kwargs)
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        price = data['price']
        data['average_price_in_region'] = average_price_in_region(price, data['region'])
        data['average_price'] = average_price(data['price'])
        return data

    #

    # НЕ ПРАЦЮЄ
    #         def validate_brand(self, brand):
    #             if not brand:
    #                 send_mail(
    #                     'Brand not available',
    #                     'The serializer did not receive any data',
    #                     'from@example.com',  # виправити на email продавця
    #                     ['manager@example.com'],
    #                     fail_silently=False,
    #                 )
    #             return brand
    # def validate(self, brand):
    #     if not brand:
    #         raise serializers.ValidationError('Brand is missing contact with manager manager@gmail.com')
    #     return brand

    # def create(self, validated_data):
    #     seller_id = validated_data['seller_id']
    #     existing_quantity = CarModel.objects.filter(seller_id=seller_id).aggregate(models.Sum('quantity'))[
    #         'quantity__sum']
    #     if existing_quantity is not None and existing_quantity + validated_data['quantity'] >= 1:
    #         raise serializers.ValidationError('Total quantity cannot be greater than 1')
    #     return super().create(validated_data)

    #
    # def update(self, instance, validated_data):
    #     seller_id = instance.seller.id
    #     new_quantity = validated_data.get('quantity', instance.quantity)
    #     existing_quantity = CarModel.objects.filter(seller_id=seller_id).exclude(id=instance.id).aggregate(models.Sum('quantity'))[
    #         'quantity_sum']
    #     if existing_quantity is not None and existing_quantity + new_quantity > 1:
    #         raise serializers.ValidationError('Total quantity cannot be greater than 1')
    #     return super().update(instance, validated_data)

    #
