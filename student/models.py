from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Student(models.Model):
    s_number = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=2)
    subject = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    ID_number = models.IntegerField()
    native_place = models.CharField(max_length=30)

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生管理"
