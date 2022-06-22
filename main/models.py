from django.db import models
from account.models import User
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name="ФИО Ментора")

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name="ФИО Студента")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=250)
    months = models.PositiveSmallIntegerField()
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(Student, through='CourseClass')

    def __str__(self):
        return self.name


class CourseClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_start = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.date_start:
            self.end_date = date.today() + relativedelta(months=self.course.months)
        super(CourseClass, self).save(*args, **kwargs)
