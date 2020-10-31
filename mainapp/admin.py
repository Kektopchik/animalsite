from django.contrib import admin

from .models import Animals

class AnimalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Animals, AnimalAdmin)

