from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.

u=User.objects.get(username__exact="Admin")
u.set_password("abcd123")
u.save()