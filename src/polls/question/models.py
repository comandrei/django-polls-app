from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text


class QuestionsChoices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    text = models.CharField(max_length=250)
    correct = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text
