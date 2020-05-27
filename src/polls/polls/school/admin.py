from django.contrib import admin

from .models import Student, Courses, Client, Reprezentant
# Register your models here.

admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Client)
admin.site.register(Reprezentant)
