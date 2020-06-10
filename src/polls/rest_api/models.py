from django.db import models
from django.contrib.auth import get_user_model


class ToDo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    completed = models.BooleanField()
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return self.title
