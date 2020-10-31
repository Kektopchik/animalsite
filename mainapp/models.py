from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    SEX_ANIMAL = (
        ('M', 'Кабель'),
        ('Ж', 'Сучка'),
    )

    name = models.CharField("Кличка", null=True, max_length=50),
    color = phone = models.CharField(max_length=30, verbose_name="Цвет животного", default=""),
    sex = models.CharField(max_length=30, verbose_name="Пол", choices=SEX_ANIMAL, default=""),