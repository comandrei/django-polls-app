from rest_framework import serializers
from question.models import Question, QuestionsChoices

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsChoices
        fields = "__all__"
