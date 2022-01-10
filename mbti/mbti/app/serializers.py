from rest_framework import serializers
from .models import Question, Choice, User, MBTI, Answer

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class MBTISerializer(serializers.ModelSerializer):
	class Meta:
		model = MBTI
		fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'