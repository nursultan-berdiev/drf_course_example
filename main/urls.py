from django.urls import path, include
from .views import StudentViewSet, MentorViewSet, CourseViewSet, CourseClassViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')
router.register('mentor', MentorViewSet, basename='mentor')
router.register('course', CourseViewSet, basename='course')
router.register('courseclass', CourseClassViewSet, basename='courseclass')

urlpatterns = [
    path('', include(router.urls)),

]