from django.shortcuts import render, redirect
from .forms import QuestionsForm,AnswersForm
from .models import Questions, Answers

# Create your views here.
def index(request):
    questions = Questions.objects.all()
    context = {
        'questions' : questions
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithor:index')
    else :
        form = QuestionsForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def detail(request, question_id):
    question = Questions.objects.get(id = question_id)
    form = AnswersForm()
    articles = question.answers_set.all()
    context = {
        'question' : question,
        'form' : form,
        'articles' : articles,
    }
    return render(request, 'detail.html', context)

def comment_create(request, question_id):
    article = Questions.objects.get(id = question_id)
    if request.method == 'POST':
        form  = AnswersForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.question = article
            form.save()
            return redirect('eithor:detail', question_id = question_id)
    else:
        form = AnswersForm()

    context ={
        'form':form
    }
    return render(request, 'detail.html', context)