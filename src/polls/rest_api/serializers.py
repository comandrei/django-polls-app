from rest_framework import serializers
from question.models import Question, QuestionsChoices
from .models import ToDo

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsChoices
        fields = "__all__"


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
