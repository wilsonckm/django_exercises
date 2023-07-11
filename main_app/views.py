from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Exercise, Workout
from django.http import HttpResponse
import requests, os

api_key = os.environ.get('API_KEY')

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

def exercise_searches(request):
    if request.method == 'POST':
        muscle = request.POST.get('muscle', '')  # Get the selected muscle from the POST data
        api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}'
        # print(request.POST)
        # print(api_url)
        # print(muscle)
        response = requests.get(api_url, headers={'X-Api-Key': api_key })
        if response.status_code == requests.codes.ok:
            exercise_searches = response.json()
            print(muscle)
            return render(request, "exercise_searches.html", {'exercise_searches': exercise_searches})
        else:
            print("Error:", response.status_code, response.text)
        
    return render(request, "exercise_searches.html")

def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    return render(request, 'workout_detail.html', {'workout': workout})

def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html', {
        'workouts': workouts
    })

