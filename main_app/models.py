from django.db import models
from django.urls import reverse

# Create your models here.

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
