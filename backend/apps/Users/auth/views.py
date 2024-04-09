from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.all_users.users.models import ProfileModel
from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from apps.all_users.users.serializers import ProfileSerializer, UserSerializer


class MeView(GenericAPIView):
    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = self.serializer_class(user.profile, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class RecoverySendEmailView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserSerializer
#
#     def post(self, *args, **kwargs):
#         email = kwargs.get('email')
#         user = get_object_or_404(UserModel, email=email)
#         EmailService.recovery_password(user)
#         return Response(status=status.HTTP_200_OK)
#
#
# class RecoverySetPasswordView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = PasswordSerializer
#
#     def post(self, *args, **kwargs):
#         token = kwargs.get('token')
#         new_password = kwargs.get('password')
#         serializer = PasswordSerializer(data={'password': new_password})
#         serializer.is_valid(raise_exception=True)
#         user = JWTService.validate_token(token, RecoveryToken)
#         user.set_password(new_password)
#         user.save()
#         return Response({'details': 'password saved'}, status=status.HTTP_200_OK)


#написати код на зміну пароля, попробувати винести інформацію  по машинах для преміум продавців
# винести код для зміни даних по товару продавця