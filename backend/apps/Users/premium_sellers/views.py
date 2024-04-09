from datetime import timedelta

from django.contrib.auth import get_user_model
from django.http import Http404
from django.utils import timezone

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.all_users.premium_sellers.models import PremiumSellerModel
from apps.all_users.premium_sellers.serializers import PremiumSellerSerializer
from apps.all_users.users.models import UserModel as User
from apps.all_users.users.serializers import UserSerializer
from apps.cars_details.cars.models import CarModel
from apps.cars_details.cars.serializers import CarSerializer, PremiumSellersCarsSerializer

# AdvertisementSerializer
# # from django.http import Http404
# # from rest_framework import status
# from django.http import Http404
# 
# from rest_framework import status
# from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# # from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# 
# from apps.cars_details.cars.models import CarModel
# from apps.cars_details.cars.serializers import CarSerializer
# 
# from .models import PremiumSellerModel
# # from rest_framework.response import Response
# # from rest_framework.mixins import ListModelMixin, CreateModelMixin
# from .serializers import PremiumSellerAllSerializer, PremiumSellerSerializer
# 
# 
# # class PremiumSellersListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
# # class PremiumSellersListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
# class PremiumSellersListCreateView(ListCreateAPIView):
#     serializer_class = PremiumSellerAllSerializer
#     # queryset = PremiumSellerModel.objects.all()
#     queryset = PremiumSellerModel.objects.prefetch_related('cars')
#     # permission_classes = (IsAuthenticated,)
#     # pagination_class = None
# 
#     # def get(self, request, *args, **kwargs):
#     #     return super().list(request, *args, **kwargs)
#     #
#     # def post(self, request, *args, **kwargs):
#     #     return super().create(request, *args, **kwargs)
# 
#     # def get(self, *args, **kwargs):
#     #     query_set = PremiumSellerModel.objects.all()
#     #     serializer = PremiumSellerSerializer(query_set, many=True)
#     #     return Response(serializer.data, status.HTTP_200_OK)
# 
#     # def post(self, *args, **kwargs):
#     #     data = self.request.data
#     #     serializer = PremiumSellerSerializer(data=data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status.HTTP_201_CREATED)
# 
# 
# class PremiumSellerUpdateRetrieveDestroyListView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PremiumSellerSerializer
#     queryset = PremiumSellerModel.objects.all()
# 
#     # class PremiumSellerCarsListCreateView(GenericAPIView):
#     #     serializer_class = PremiumSellerSerializer
#     #     queryset = PremiumSellerModel.objects.all()
#     #
#     #     def get(self, *args, **kwargs):
#     #         pk = kwargs['pk']
#     #         exist = PremiumSellerModel.objects.filter(pk=pk).exists()
#     #         if not exist:
#     #             raise Http404()
#     #         cars = CarModel.objects.filter(premium_seller_id=pk)
#     #         serializer = CarSerializer(cars, many=True)
#     #         return Response(serializer.data, status.HTTP_200_OK)
#     #
#     #     def post(self, *args, **kwargs):
#     #         pk = kwargs['pk']
#     #         data = self.request.data
#     #         serializer = CarSerializer(data=data)
#     #         serializer.is_valid(raise_exception=True)
#     #         exists = PremiumSellerModel.objects.filter(pk=pk).exists()
#     #         if not exists:
#     #             raise Http404()
#     #         serializer.save(premium_seller_id=pk)
#     #         return Response(serializer.data, status.HTTP_201_CREATED)
# 
# 
# class PremiumSellerCarsListCreateView(GenericAPIView):
#     # serializer_class = PremiumSellerSerializer
#     queryset = PremiumSellerModel.objects.all()
# 
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
# 
#         exists = PremiumSellerModel.objects.filter(pk=pk).exists()
#         if not exists:
#             raise Http404()
# 
#         cars = CarModel.objects.filter(premium_seller_id=pk)
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
# 
#     def post(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         # premium_seller = self.get_object()
#         exists = PremiumSellerModel.objects.filter(pk=pk).exists()
#         if not exists:
#             raise Http404()
#         serializer.save(premium_seller_id=pk)
#         return Response(serializer.data, status.HTTP_201_CREATED)
# 
# 
# class PremiumSellerCarsUpdateRetrieveDestroyListView(RetrieveUpdateDestroyAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#     lookup_field = 'cars_id'  # перевірити чи працює


UserModel: User = get_user_model()


class PremiumSellerListView(ListAPIView):
    # queryset = UserModel.objects.filter(roles='premium_seller')
    # serializer_class = UserSerializer
    queryset = PremiumSellerModel.objects.all()
    serializer_class = PremiumSellerSerializer


class PremiumSellerView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.filter(roles='premium_seller')
    # queryset = PremiumSellerModel.objects.all()
    # serializer_class = PremiumSellerSerializer
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return (IsAuthenticated(),)


class PremiumSellerCarsListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.filter(roles='premium_seller')
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        exist = UserModel.objects.filter(pk=pk).exists()
        if not exist:
            raise Http404()
        cars = CarModel.objects.filter(premium_seller_id=pk)
        serializer = PremiumSellersCarsSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        serializer = PremiumSellersCarsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            raise Http404()
        serializer.save(premium_seller_id=pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class PremiumSellerListView()
# class PremiumSellerListAndCarsView(ListAPIView):
#     queryset = UserModel.objects.filter(roles='premium_seller')
#     serializer_class = UserSerializer
#
#     def all_users_info(request):
#         users = UserModel.objects.all()
#         user_data = []
#
#         for user in users:
#             cars = CarModel.objects.filter(user=user)
#             total_views = sum(car.car_views for car in cars)
#
#             user_info = {
#                 'id': user.id,
#                 'email': user.email,
#                 'cars': [
#                     {
#                         'brand': 'car.brand',
#                         'car_views': 'cars.car_views'}
#                     for car in cars],
#                 'total_views': total_views
#             }
#             user_data.append(user_info)
#
#         return Response(data=user_data, status=status.HTTP_200_OK)
class PremiumSellerStatisticListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = PremiumSellersCarsSerializer


# @api_view(['GET'])
# def get_view_counts(request, user_id):
#     today = timezone.now().date()
#     week_ago = today - timedelta(days=7)
#     month_ago = today - timedelta(days=30)
#
#     daily_count = CarView.objects.filter(user_id=user_id, timestamp__date=today).count()
#     weekly_count = CarView.objects.filter(user_id=user_id, timestamp__date__range=[week_ago, today]).count()
#     monthly_count = CarView.objects.filter(user_id=user_id, timestamp__date__range=[month_ago, today]).count()
#
#     return Response({
#         'daily_count': daily_count,
#         'weekly_count': weekly_count,
#         'monthly_count': monthly_count
#     })
