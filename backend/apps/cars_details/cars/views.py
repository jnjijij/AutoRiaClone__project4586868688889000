from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

# from .filters import car_filtered_queryset
# from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return (IsAuthenticated(),)
    # filterset_class = CarFilter # не працюють фільтри тому що в моделях майже всі поля закоментовані


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return (IsAuthenticated(),)
