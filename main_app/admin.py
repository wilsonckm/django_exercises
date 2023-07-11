from django.contrib import admin
from .models import Exercise, ExerciseInWorkout

# Register your models here.

from .models import Exercise

admin.site.register(Exercise)
admin.site.register(ExerciseInWorkout)
