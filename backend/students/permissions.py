from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):

    def has_permission(self, request, view):

        role = request.headers.get('role')

        if role == "HOD":
            return True

        if role == "TEACHER":
            return request.method in ['GET','POST']

        if role == "STUDENT":
            return request.method == 'GET'

        return False