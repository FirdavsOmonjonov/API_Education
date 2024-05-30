from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from datetime import datetime
import io
from rest_framework.parsers import JSONParser
from .models import Course, Teacher, Student



class CourseSerializer(serializers.Serializer):
    """Serializer for Course"""
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=111)
    price = serializers.IntegerField()
    countinum = serializers.IntegerField()


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.countinum = validated_data.get('countinum', instance.countinum)
        instance.save()
        return instance

class TeacherSerializer(serializers.Serializer):
    """Serializer for Teacher"""
    id = serializers.ReadOnlyField()
    f_name = serializers.CharField(max_length=100)
    l_name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    experience = serializers.IntegerField()
    course_id = serializers.IntegerField()


    def update(self, instance, validated_data):
        instance.f_name = validated_data.get('f_name', instance.f_name)
        instance.l_name = validated_data.get('l_name', instance.l_name)
        instance.status = validated_data.get('status', instance.status)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.save()
        return instance

class StudentSerializer(serializers.Serializer):
    """Serializer for Student"""
    id = serializers.ReadOnlyField()
    f_name = serializers.CharField(max_length=100)
    l_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=14)
    parent_phone_number = serializers.CharField(max_length=14)
    telegram_link = serializers.CharField(max_length=100)
    course_id = serializers.IntegerField()
    teacher_id = serializers.IntegerField()


   
    def update(self, instance, validated_data):
        instance.f_name = validated_data.get('f_name', instance.f_name)
        instance.l_name = validated_data.get('l_name', instance.l_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.parent_phone_number = validated_data.get('parent_phone_number', instance.parent_phone_number)
        instance.telegram_link = validated_data.get('telegram_link', instance.telegram_link)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.teacher_id = validated_data.get('teacher_id', instance.teacher_id)
        instance.save()
        return instance

