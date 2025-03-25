from django.forms import ModelForm
from .models import Questions, Answers

class QuestionsForm(ModelForm):
    class Meta():
        model = Questions
        fields = '__all__'

class AnswersForm(ModelForm):
    class Meta():
        model = Answers
        fields = ('answer', 'content',)