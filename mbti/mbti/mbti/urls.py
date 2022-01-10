"""mbti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import QuestionListCreateAPIView, QuestionRetrieveUpdateDestroyAPIVIew, ChoiceListCreateAPIView, ChoiceRetrieveUpdateDestroyAPIVIew, UserListCreateAPIView, UserRetrieveUpdateDestroyAPIVIew, MBTIListCreateAPIView, MBTIRetrieveUpdateDestroyAPIVIew, AnswerListCreateAPIView, AnswerRetrieveUpdateDestroyAPIVIew
from app.views import GetChoicePerMBTI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/', QuestionListCreateAPIView.as_view()),
    path('question/<question_pk>', QuestionRetrieveUpdateDestroyAPIVIew.as_view()),
    path('choice/', ChoiceListCreateAPIView.as_view()),
    path('choice/<choice_pk>', ChoiceRetrieveUpdateDestroyAPIVIew.as_view()),
    path('user/', UserListCreateAPIView.as_view()),
    path('user/<user_pk>', UserRetrieveUpdateDestroyAPIVIew.as_view()),
    path('mbti/', MBTIListCreateAPIView.as_view()),
    path('mbti/<mbti_pk>', MBTIRetrieveUpdateDestroyAPIVIew.as_view()),
    path('answer/', AnswerListCreateAPIView.as_view()),
    path('answer/<answer_pk>', AnswerRetrieveUpdateDestroyAPIVIew.as_view()),
    path('per/', GetChoicePerMBTI.as_view()),
]
