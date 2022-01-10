from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

# Create your views here.
class StudentListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()
	
class StudentRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()
	lookup_url_kwarg = 'student_pk'