from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle = models.CharField(max_length=100)
    set = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()
    cooldown_period= models.IntegerField(default=2)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'exercise_id': self.id})
    
class Workout(models.Model):
    date = models.DateField()
    time = models.TimeField()
    exercises = models.ManyToManyField(Exercise, through='ExerciseInWorkout')  # Many-to-many relationship with Exercise model

    def __str__(self):
        return f'{self.date} ({self.id})'

    def get_absolute_url(self):
        return reverse('workout_detail', kwargs={'workout_id': self.id})


class ExerciseInWorkout(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    last_performed = models.DateTimeField(null=True, blank=True)  # Track the last time the exercise was performed in the workout

    def __str__(self):
        return f'{self.exercise} in {self.workout}'

    def calculate_next_performance(self):
        cooldown_period = self.exercise.cooldown_period
        if self.last_performed:
            next_performance = self.last_performed + timezone.timedelta(days=cooldown_period)
        else:
            next_performance = timezone.now()  # If exercise has never been performed in the workout, set next performance as current time
        return next_performance