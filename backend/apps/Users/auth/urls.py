from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import MeView, UpdateUserProfileView

# MeChangeView
urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/me', MeView.as_view()),
    path('/me/change/<int:pk>', UpdateUserProfileView.as_view())
]