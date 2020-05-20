from django.shortcuts import render
from .models import QuestionnairesQuestions
from question.models import QuestionsChoices, Question
from django.http import HttpResponse


def send_questionnaire(request, id):
    if request.method == 'POST':
        answers = request.POST
        correct_answers = 0
        for answer in answers:
            if 'csrfmiddlewaretoken' != answer:
                question_choices = QuestionsChoices.objects.filter(question=answer)
                for question_choice in question_choices:
                    if question_choice.id == int(answers[answer]) and question_choice.correct:
                        correct_answers += 1
        return HttpResponse("Correct answers: " + str(correct_answers))

    questionnaire_questions = QuestionnairesQuestions.objects.filter(questionnaire=id)
    return render(request, 'questionnaire/send.html', {
        'questionnaire_questions': questionnaire_questions
    })
