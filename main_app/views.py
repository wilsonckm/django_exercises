from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exercise

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def exercise_index(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/index.html', {
        'exercises': exercises
    })

def exercise_detail(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    return render(request, 'exercises/detail.html', {
        'exercise': exercise
    })

class ExerciseCreate(CreateView):
    model = Exercise
    fields = '__all__'

class ExerciseUpdate(UpdateView):
    model = Exercise
    fields = ['name', 'muscle', 'set', 'reps', 'weight']

class ExerciseDelete(DeleteView):
    model = Exercise
    success_url='/exercises'

# Create your views here.
