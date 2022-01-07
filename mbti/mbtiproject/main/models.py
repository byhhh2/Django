from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    memo = models.TextField()

    # name이 User object 대신하기
    def __str__(self):
        return self.name