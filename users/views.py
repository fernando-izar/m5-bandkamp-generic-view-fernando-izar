from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
