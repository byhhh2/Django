from django.shortcuts import render
from .models import Question, Choice, User, MBTI, Answer
from .serializers import QuestionSerializer, ChoiceSerializer, UserSerializer, MBTISerializer, AnswerSerializer
from rest_framework import generics
# Create your views here.

class QuestionListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	
class QuestionRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	lookup_url_kwarg = 'question_pk'

class ChoiceListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = ChoiceSerializer
	queryset = Choice.objects.all()
	
class ChoiceRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ChoiceSerializer
	queryset = Choice.objects.all()
	lookup_url_kwarg = 'choice_pk'

class UserListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	
class UserRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	lookup_url_kwarg = 'user_pk'

class MBTIListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = MBTISerializer
	queryset = MBTI.objects.all()
	
class MBTIRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = MBTISerializer
	queryset = MBTI.objects.all()
	lookup_url_kwarg = 'mbti_pk'

class AnswerListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = AnswerSerializer
	queryset = Answer.objects.all()
	
class AnswerRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = AnswerSerializer
	queryset = Answer.objects.all()
	lookup_url_kwarg = 'answer_pk'

class GetChoicePerMBTI(generics.ListCreateAPIView):
	serializer_class = AnswerSerializer
	queryset = Answer.objects.filter(choice = 1).filter(user__mbti = "entp") #1
