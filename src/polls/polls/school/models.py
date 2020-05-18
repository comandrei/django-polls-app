from django.db import models

from django.contrib.auth.models import User

from django.db.transaction import atomic
# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    an = models.IntegerField()
    courses = models.ManyToManyField(Courses)
    bani = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
