from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render
from .serializers import StudentSerializer, MentorSerializer, CourseClassSerializer, CourseSerializer
from .permisions import IsOwnerOrIsAdmin, IsMentorOrAdmin
from .models import Student, Mentor, CourseClass, Course


class MentorViewSet(ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsOwnerOrIsAdmin, ]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsOwnerOrIsAdmin, ]


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsMentorOrAdmin, ]


class CourseClassViewSet(ModelViewSet):
    queryset = CourseClass.objects.all()
    serializer_class = CourseClassSerializer
    permission_classes = [IsMentorOrAdmin, ]