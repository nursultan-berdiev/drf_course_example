from rest_framework import serializers
from .models import Student, Mentor, CourseClass, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ['user', ]


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "__all__"
        read_only_fields = ['user', ]


class CourseClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseClass
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ['mentor', ]
