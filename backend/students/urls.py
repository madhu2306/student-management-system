from django.urls import path
from . import views

urlpatterns = [
path('register/', views.register),
path('login/', views.login),
path('students/', views.students),
path('students/<int:id>/', views.student_update),
]