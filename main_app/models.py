from django.db import models
from django.urls import reverse

# Create your models here.
SESSIONS = (
    ('A', 'Aerobics'),
    ('B', 'Boxing'),
    ('C', 'Cardio'),
    ('P', 'Pilates'),
    ('S', 'Swimming'),
    ('W', 'Weightlifting'),
    ('Y', 'Yoga')
)
session = models.CharField(max_length=20, choices=SESSIONS)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle = models.CharField(max_length=100)
    set = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'exercise_id': self.id})

class Workout(models.Model):
    date = models.DateField()
    session = models.CharField(
        max_length=1,
        choices=SESSIONS,
        default='SESSIONS'[0][0]
    )
    # Create a exercise_id ForeignKey
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_session_display()} on {self.date}"
