from django.contrib import admin
from .models import Question, QuestionsChoices


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'updated_at')
    list_filter = ('text', 'created_at', 'updated_at')
    search_fields = ('text', 'created_at', 'updated_at')
    list_per_page = 10


@admin.register(QuestionsChoices)
class QuestionsChoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'correct', 'created_at', 'updated_at')
    list_filter = ('text', 'question', 'correct', 'created_at', 'updated_at')
    search_fields = ('text', 'question', 'correct', 'question', 'correct', 'question', 'correct', 'created_at', 'updated_at')
    list_per_page = 10
