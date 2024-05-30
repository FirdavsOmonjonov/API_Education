from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import  Course, Teacher, Student


@admin.register(Course)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'countinum', )
    list_display_link = ('id', 'name')


@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'l_name', 'status', 'experience', 'course')
    list_display_links = ('id', 'f_name', 'l_name')


@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'l_name', 'phone_number', 'parent_phone_number', 'telegram_link', 'course', 'teacher')
    list_display_links = ('id', 'f_name', 'l_name')
