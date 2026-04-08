from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Student
from .serializers import UserSerializer, StudentSerializer
from .permissions import RolePermission
from django.shortcuts import get_object_or_404


# REGISTER
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# LOGIN
@api_view(['POST'])
def login(request):

    username = request.data.get("username","").strip()
    password = request.data.get("password","").strip()

    try:
        user = User.objects.get(
            username=username,
            password=password
        )

        return Response({
            "username": user.username,
            "role": user.role
        })

    except User.DoesNotExist:
        return Response(
            {"error":"Invalid username or password"},
            status=400
        )


# GET + ADD
@api_view(['GET','POST'])
@permission_classes([RolePermission])
def students(request):

    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# UPDATE + DELETE
@api_view(['PUT','DELETE'])
@permission_classes([RolePermission])
def student_update(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        student.delete()
        return Response({"deleted": True})