from django.db import models
from question.models import Question


class Questionnaire(models.Model):
    text = models.CharField(max_length=250)
    active = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{}: {}".format(str(self.id), self.text)


class QuestionnairesQuestions(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.questionnaire.text
