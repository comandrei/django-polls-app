from django.urls import path

from .views import index, list_student, carnet_note, form_client
urlpatterns = [
    path('', index),
    path('form/<int:id>', form_client),
    path('form', form_client),

    path('students/<int:cucu_student_id>', carnet_note, name="carnet-note"),
    path('students', list_student)
]