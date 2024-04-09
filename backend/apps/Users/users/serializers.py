from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

# from apps.Users.users.models import RolesModel
from apps.all_users.users.models import UserModel as User

from ...cars_details.cars.serializers import CarSerializer
# from ..sellers.serializers import SellerSerializer
from .models import ProfileModel

UserModel: User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'user',)
        read_only_fields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_superuser', 'is_staff', 'created_at', 'updated_at',
            'last_login', 'profile', 'roles', 'cars'
        )
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'is_superuser', 'last_login', 'is_active', 'cars')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
