from django.urls import path

from .views import index, list_student, carnet_note
urlpatterns = [
    path('', index),
    path('students/<int:cucu_student_id>', carnet_note, name="carnet-note"),
    path('students', list_student)
]