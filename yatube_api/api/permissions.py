from rest_framework import permissions

YOU_CANNOT = 'У вас недостаточно прав для данного действия.'


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = YOU_CANNOT

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
