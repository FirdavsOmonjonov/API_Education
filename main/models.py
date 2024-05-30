from django.db import models

class Course(models.Model):
    """Model for Course"""
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    countinum = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price * self.countinum


class Teacher (models.Model):
    """Model for Teacher"""
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    experience = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.f_name + " " + self.l_name


class Student (models.Model):
    """Model for Student"""
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    parent_phone_number = models.CharField(max_length=14)
    telegram_link = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name + " " + self.l_name