from django.urls import path

from .views import UserListCreateView, UserListRetrieveUpdateDestroyView  # UsersListView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    # path('/see_all', UsersListView.as_view()),
    path('/<int:pk>', UserListRetrieveUpdateDestroyView.as_view()),
    # path('/<int:pk>/cars', SellerCarsListCreateView.as_view())
    # path('/my', MyView.as_view()),
    # path('/roles', RolesCreateAPIView.as_view())
    # path('/add_sellers', SellerListCreateView.as_view())
]
