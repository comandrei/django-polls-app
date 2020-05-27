from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class TimeTrackerModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
class CourseManager(models.Manager):

    def seniors(self):
        return self.filter(an=4)

    def juniors(self):
        return self.filter(an__in=[1, 2])

class Courses(TimeTrackerModel):

    class Meta:
        ordering = ("an", "-title")
        get_latest_by = ("modified_at", )
        unique_together = ("title", "an")

    title = models.CharField(max_length=100, unique=True)
    an = models.IntegerField()

    objects = CourseManager()

    def __str__(self):
        return self.title + ' ' + str(self.an) 


# Courses.objects.filter(an=4)
# Courses.objects.seniors()

class Student(TimeTrackerModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    an = models.IntegerField()
    courses = models.ManyToManyField(Courses)
    bani = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


# for course in Courses.objects.all():
#     course.an = course.an + 1
#     course.save() # update courses set an = x where id = x.id


# update courses set an = an + 1 

FUNCTII = (1, 'Director',
           2, 'Presedinte',
           3, 'Administrator')

class Reprezentant(models.Model):
    nume = models.CharField(max_length=255)
    prenume = models.CharField(max_length=255)
    email = models.EmailField()
    telefon = models.IntegerField()
    functie = models.IntegerField()

class Client(models.Model):
    nume = models.CharField(max_length=255)
    adresa = models.CharField(max_length=255)
    cui = models.IntegerField()
    reprezentant = models.ForeignKey(Reprezentant, on_delete=models.CASCADE)

