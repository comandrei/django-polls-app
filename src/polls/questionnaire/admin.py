from django.contrib import admin
from .models import Questionnaire, QuestionnairesQuestions


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'text', 'created_at', 'updated_at')
    list_filter = ('text', 'active', 'created_at', 'updated_at')
    search_fields = ('text', 'active', 'created_at', 'updated_at')
    list_per_page = 10


@admin.register(QuestionnairesQuestions)
class QuestionnairesQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'questionnaire', 'question', 'created_at', 'updated_at')
    list_filter = ('questionnaire', 'question', 'created_at', 'updated_at')
    search_fields = ('questionnaire', 'question', 'created_at', 'updated_at')
    list_per_page = 10
