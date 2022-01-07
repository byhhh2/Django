from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def dashboard(request):
    userlist = User.objects.all() ## 모든 유저 
    # dashboard.html 페이지를 열 때, userList도 가져옴 
    return render(request, 'main/dashboard.html', {'userlist': userlist})

def user(request, pk):
  user = User.objects.get(pk = pk)
  # user.html 페이지를 열 때, 특정 user를 가져옴 
  return render(request, 'main/user.html', {'user': user})

def new_user(request):
  if request.method == 'POST':
    new_info = User.objects.create(
        name = request.POST['name'],
        memo = request.POST['memo'],
    )
    return redirect('/dashboard/')
  return render(request, 'main/new_user.html')