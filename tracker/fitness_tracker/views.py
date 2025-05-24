from rest_framework  import viewsets
from .models import Workout, CustomExercise

from .serializers import WorkoutSerializer
from .forms import WorkoutForm, CustomExerciseForm, WorkoutExerciseFormSet

from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages



def add_exercise(request):
    if request.method == 'POST':
        form = CustomExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exercise added successfully!')
            return redirect('home')
    else:
        form = CustomExerciseForm()
    return render(request, 'add_exercise.html', {'form': form})

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

def get_exercise_types(request):
    workout_type = request.GET.get('type')
    if workout_type == 'cardio':
        choices = Workout.CARDIO_TYPES
    elif workout_type == 'calisthenics':
        choices = Workout.CALISTHENICS_TYPES
    elif workout_type == 'weightlifting':
        choices = Workout.WEIGHTLIFTING_TYPES
    else:
        choices = []
    
    custom_exercises = CustomExercise.objects.filter(category=workout_type)
    for exercise in custom_exercises:
        choices.append((f'custom_{exercise.id}',f'Custom: {exercise.name}'))

    return JsonResponse({'choices': choices})

def workout_details(request, workout_id):
    workout = get_object_or_404(Workout, id = workout_id)

    if request.method == 'POST':
        formset = WorkoutExerciseFormSet(request.POST, instance=workout)
        if formset.is_valid():
            formset.save()
            return redirect('workout_details', workout_id=workout_id)
    else:
        formset = WorkoutExerciseFormSet(instance=workout)

    return render(request, 'workout_details.html', {
        'workout': workout,
        'formset': formset
    })


