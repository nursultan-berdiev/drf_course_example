from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import StudentCreateAPIView, MentorCreateAPIView

urlpatterns = [
    path('create/student/', StudentCreateAPIView.as_view(), name='student_create'),
    path('create/mentor/', MentorCreateAPIView.as_view(), name='student_create'),
    path('token/', obtain_auth_token, name="token"),
]