from rest_framework import serializers
from .models import User
from main.models import Student, Mentor

from main.serializers import StudentSerializer, MentorSerializer


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128)

    def validate(self, data):
        if data['password2'] != data['password']:
            raise serializers.ValidationError("Пароли должны совпадать")
        return data


class StudentCreateSerializer(UserSerializer):
    student = StudentSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'student']

    def save(self):
        user = User(username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        try:
            Student.objects.create(user=user, name=self.validated_data['student']['name'])
        except Exception as e:
            print(e)
            user.delete()
        else:
            return user


class MentorCreateSerializer(UserSerializer):
    mentor = MentorSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'mentor']

    def save(self):
        user = User(username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        try:
            Mentor.objects.create(user=user, name=self.validated_data['mentor']['name'])
        except Exception as e:
            print(e)
            user.delete()
        else:
            return user
