from django.forms import ModelForm, Textarea
from .models import Questions, Answers
from django import forms


class QuestionsForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs = {'class':'form-control'}
        )
    )
    class Meta():
        model = Questions
        fields = '__all__'
        widgets = {
            'option_a' : Textarea(attrs={'class':'form-control'}),
            'option_b' : Textarea(attrs={'class':'form-control'}),
        }

class AnswersForm(ModelForm):
    # title = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs = {'class':'form-control'}
    #     )
    # )
    class Meta():
        model = Answers
        fields = ('answer', 'content',)
        widgets = {
            'content' : Textarea(attrs={'class':'form-control'})
        }