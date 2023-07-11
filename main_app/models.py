from django.db import models
from django.urls import reverse
from datetime import time

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle = models.CharField(max_length=100)
    set = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()

    workout = models.ForeignKey('Workout', on_delete=models.CASCADE, default='Workout.objects.first()')
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'exercise_id': self.id})
    
class Workout(models.Model):
    date = models.DateField()
    time = models.TimeField(
        default=time(hour=8, minute=0)
    )

    def __str__(self) -> str:
        return f'{self.name} ({self.id})'
    

