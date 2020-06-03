from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def clean_text(self):
        data = self.cleaned_data['text']
        if "bubu" in data.lower():
            raise forms.ValidationError("Cannot contain bubu!")
        return data

