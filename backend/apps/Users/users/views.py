from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.pagination import PagePagination

from apps.all_users.users.models import UserModel as User

from ...cars_details.cars.models import CarModel
from ...cars_details.cars.serializers import CarSerializer
from ..sellers.models import SellerModel
from .filters import UserFilter
from .serializers import UserSerializer

UserModel: User = get_user_model()


# class UserListCreateView(ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()
# class RolesCreateAPIView(ListCreateAPIView):
#     serializer_class = RoleSerializer
#     queryset = RolesModel.objects.all()


# class UserListCreateView(ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    # permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == 'POST':
            return (AllowAny(),)
        return (IsAdminUser(),)
    # pagination_class = PagePagination


# class UsersListView(ListAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()
#     permission_classes = (IsAdminUser,)
#     filterset_class = UserFilter
#     pagination_class = PagePagination


class UserListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)
    filterset_class = UserFilter
    pagination_class = PagePagination

# class MyView(GenericAPIView):
#     serializer_class = UserSerializer
#
#     def get_object(self):
#         return self.request.user
#
#     def get(self, *args, **kwargs):
#         serializer = UserSerializer(self.get_object())
#         return Response(serializer.data, status.HTTP_200_OK)

# .filter(is_superuser=False))
# filterset_class = UserFilters
# def get_queryset(self):
#     return User.objects.filter(roles='seller')

# def filter_queryset(self, queryset):
#     return super().filter_queryset(queryset).distinct()

# class SellerListCreateView(GenericAPIView):
#     serializer_class = SellerSerializer
#     queryset = SellerModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         user = self.request.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data['sellers'], status=status.HTTP_200_OK)
#
#     # def post(self, *args, **kwargs):
#     #     user = self.request.user
#     #     data = self.request.data
#     #     serializer = self.serializer_class(data=data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save(user=user)
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def post(self, *args, **kwargs):
#         user = self.request.user
#         data = self.request.data
#         serializer = SellerSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         sellers: SellerModel = serializer.save()
#         sellers.users.add(user)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     # def post(self, *args, **kwargs):
#     #     user = self.request.user
#     #     data = self.request.data
#     #     serializer = self.serializer_class(data=data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save(user=user)
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class SellerCarsListCreateView(GenericAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         exist = UserModel.objects.filter(pk=pk).exists()
#         if not exist:
#             raise Http404()
#         cars = SellerModel.objects.filter(seller_id=pk)
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         exists = UserModel.objects.filter(pk=pk).exists()
#         if not exists:
#             raise Http404()
#         serializer.save(seller_id=pk)
#         return Response(serializer.data, status.HTTP_201_CREATED)
