from rest_framework import viewsets

from .serializers import QuestionSerializer, ChoiceSerializer, ToDoSerializer
from question.models import Question, QuestionsChoices
from .models import ToDo


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        filter_text = self.request.query_params.get('text', '')
        return self.queryset.filter(text__icontains=filter_text)


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = QuestionsChoices.objects.all()

    def get_queryset(self):
        question_id = int(self.request.query_params.get('question_id', 0))
        if question_id:
            return self.queryset.filter(question__pk=question_id)
        return self.queryset


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     return s
