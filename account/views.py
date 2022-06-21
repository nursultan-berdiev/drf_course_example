from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import StudentCreateSerializer, MentorCreateSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class MentorCreateAPIView(UserCreateAPIView):
    serializer_class = MentorCreateSerializer


class StudentCreateAPIView(UserCreateAPIView):
    serializer_class = StudentCreateSerializer
