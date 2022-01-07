from django.contrib import admin
from django.urls import path
from .views import *

app_name='main'

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', index, name='index'),
  path('dashboard/', dashboard, name='dashboard'),
  path('user/<int:pk>/',user, name='user'),
  path('dashboard/new_user/', new_user),
]