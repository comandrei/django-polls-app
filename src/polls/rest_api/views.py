from rest_framework import viewsets

from .serializers import QuestionSerializer
from question.models import Question

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
