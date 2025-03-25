from django.db import models

# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=100)
    option_a = models.TextField()
    option_b = models.TextField()

class Answers(models.Model):
    answer_choice = [
        ('A','A'),
        ('B','B'),
    ]
    answer = models.CharField(max_length=1, choices=answer_choice, default='A')
    content = models.TextField()
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)