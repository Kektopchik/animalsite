from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    name = models.CharField("Кличка", null=True, max_length=50)
