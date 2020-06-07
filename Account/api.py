from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, LoginSerializer #RegisterSerializer,
from django.contrib.auth import get_user_model
User = get_user_model()


# # Login API
# class LoginAPI(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         _, token = AuthToken.objects.create(user,)
#         return Response({
#             "user": UserSerializer(user).data,
#             "token": token,
#             "message": " ok"
#         })

# Get User API


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LoginAPIAuth(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user,)
        return Response({
            "user": UserSerializer(user).data,
            "token": token,
        })
