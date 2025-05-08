from rest_framework  import viewsets
from rest_framework import status
from .models import Workout

from .serializers import WorkoutSerializer
from .forms import WorkoutForm

from django.shortcuts import redirect, render, get_object_or_404

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.all()

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
        form = WorkoutForm()
    return render(request, 'add_workout.html', {'form': form})

def del_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        workout.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'workout': workout})

def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'edit_workout.html', {'form':form, 'workout':workout})
 
    