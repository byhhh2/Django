from django.contrib import admin

# Register your models here.
from .models import User

# Register your models here.
# 관리자(admin)가 User에 접근 가능
admin.site.register(User)