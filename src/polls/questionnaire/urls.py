from django.urls import path, include
from . import views

urlpatterns = [
    path('send/<int:id>', views.send_questionnaire, name='send_questionnaire'),
]
