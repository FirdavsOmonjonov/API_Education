"""
URL configuration for Education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import CourseList, CourseDetail, TeacherList, TeacherDetail, StudentList, StudentDetail
urlpatterns = [
    path('admin/', admin.site.urls),
    #----------------Courses----------------
    path('api/v1/course-list/', CourseList.as_view(), name='course-list'),
    path('api/v1/course-list/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    #----------------Teacher----------------
    path('api/v1/teacher-list/', TeacherList.as_view(), name='teacher-list'),
    path('api/v1/teacher-list/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    #----------------Student----------------
    path('api/v1/student-list/', StudentList.as_view(), name='student-list'),
    path('api/v1/student-list/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
]
