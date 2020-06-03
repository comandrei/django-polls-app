from django.db import models


class Question(models.Model):
    class Meta:
        verbose_name = "Intrebare"
        verbose_name_plural = "Intrebari"

    text = models.CharField(max_length=250, help_text="Text la intrebare")
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
