from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # Note SAFE_METHODS contains GET, OPTIONS, and HEAD
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
