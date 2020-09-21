from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LogInSerializer, UserSerializer


class SignUpView(generics.CreateAPIView):
    """ Signup view for users """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    """ Custom Login view for users """
    serializer_class = LogInSerializer
