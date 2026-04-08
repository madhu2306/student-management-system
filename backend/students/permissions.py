from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class RolePermission(BasePermission):

    def has_permission(self, request, view):

        role = request.headers.get('role')

        # No role
        if not role:
            raise PermissionDenied("No role provided")

        # HOD → full access
        if role == "HOD":
            return True

        # TEACHER → GET + POST only
        if role == "TEACHER":
            if request.method in ['GET','POST']:
                return True
            raise PermissionDenied("Teacher cannot modify/delete")

        # STUDENT → only GET
        if role == "STUDENT":
            if request.method == 'GET':
                return True
            raise PermissionDenied("Student not allowed to add")

        raise PermissionDenied("Invalid role")