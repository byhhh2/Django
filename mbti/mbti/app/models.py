from django.db import models

# Create your models here.
class MBTI(models.Model):
    name = models.CharField(max_length = 4, primary_key = True)

class User(models.Model):
    name = models.CharField(max_length = 20)
    mbti = models.ForeignKey(MBTI, on_delete = models.CASCADE)

class Question(models.Model): 
    content = models.CharField(max_length = 200)

class Choice(models.Model):
    content = models.CharField(max_length = 200)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)