from rest_framework import permissions
from .models import Mentor


class IsOwnerOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        if obj.user == request.user and request.method != "DELETE":
            return True
        if request.user.is_staff:
            return True


class IsMentorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and Mentor.objects.filter(user=request.user).exists() or request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and Mentor.objects.filter(user=request.user).exists():
            mentor = Mentor.objects.get(user=request.user)
            if obj.mentor == mentor:
                return True
        if request.user.is_staff:
            return True
