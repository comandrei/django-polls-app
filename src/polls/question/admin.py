from django.contrib import admin
from .models import Question, QuestionsChoices
from .forms import QuestionForm


class ChoiceInline(admin.TabularInline):
    model = QuestionsChoices
    max_num = 4
    min_num = 2
    extra = 0
    verbose_name = "Raspunsuri la intrebare"
    verbose_name_plural = "Raspunsuri la intrebare"
    can_delete = False


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'correct_choice', 'created_at', 'updated_at')
    list_filter = ('text', 'created_at', 'updated_at')
    search_fields = ('text', 'created_at', 'updated_at')
    list_per_page = 10
    inlines = [ChoiceInline]
    form = QuestionForm

    def get_queryset(self, request):
        data = super().get_queryset(request=request)
        if request.user.is_superuser:
            return data
        else:
            return data.filter(text__icontains='Bubu')

    def correct_choice(self, obj):
        return obj.questionschoices_set.get(correct=True)
    correct_choice.short_description = "Raspunsul corect"


class QuestionsChoicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'correct', 'created_at', 'updated_at')
    list_filter = ('text', 'question', 'correct', 'created_at', 'updated_at')
    search_fields = ('text', 'question', 'correct', 'question', 'correct', 'question', 'correct', 'created_at', 'updated_at')
    list_per_page = 10
