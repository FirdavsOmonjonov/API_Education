from urllib.request import Request
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Teacher, Student
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .serializers import CourseSerializer, TeacherSerializer, StudentSerializer
from rest_framework import generics

class CourseList(generics.ListCreateAPIView):
    """Course list view"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """Course CRUD view"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TeacherList(generics.ListCreateAPIView):
    """Teacher list view"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    """Teacher CRUD view"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentList(generics.ListCreateAPIView):
    """Student list view"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Student CRUD view"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]