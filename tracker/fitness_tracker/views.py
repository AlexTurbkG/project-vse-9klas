from rest_framework  import viewsets
from rest_framework import status
from .models import Workout

from .serializers import WorkoutSerializer
from .forms import WorkoutForm

from django.shortcuts import redirect, render


def home(request):
    workouts = Workout.objects.all()
    return render(request, 'home.html', {'workouts': workouts})

def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = WorkoutForm
        return render(request, 'add_workout.html', {'form': form})

    
    