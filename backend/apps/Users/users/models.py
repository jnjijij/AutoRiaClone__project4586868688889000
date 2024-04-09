from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from .managers import UserManager
from .roles_choices import RolesChoices


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ('id',)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    roles = models.CharField(max_length=17, choices=RolesChoices.choices)
    # cars = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars')
    USERNAME_FIELD = 'email'

    objects = UserManager()

    # def filter_by_roles(self, roles):
    #     return self.filter(roles=roles)



class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    phone_number = models.IntegerField(unique=True, null=True, blank=True)
    company_name = models.CharField(max_length=25, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    # role = models.OneToOneField(RolesModel, on_delete=models.CASCADE, related_name='+')
    # roles = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='auth_user')

# class ProfileModel(models.Model):
#     class Meta:
#         db_table = 'profile'
# age = models.IntegerField(validators=[
#     val.MinValueValidator(1), val.MaxValueValidator(100)
# ])
# house = models.CharField(max_length=30)
# phone = models.CharField(max_length=15, validators=[
#     val.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.message)
# ])
# avatar = models.ImageField(upload_to=upload_avatar, blank=True)
# user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
