from django.db import models

class CustomExercise(models.Model):
    CATEGORY_TYPES = [
        ('cardio', 'Cardio'),
        ('calisthenics', 'Calisthenics'),
        ('weightlifting_upper', 'Weightlifting Upper Body'),
        ('weightlifting_lower', 'Weightlifting Lower Body'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.name}"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(CustomExercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.exercise.name} - {self.reps} reps at {self.weight}kg"

class Workout(models.Model):
    WORKOUT_TYPES = [
        ('cardio', 'Cardio'),
        ('weightlifting', 'Weightlifting'),
        ('calisthenics', 'Calisthenics'),
        ('stretching', 'Stretching'),
    ]

    CARDIO_TYPES = [
        ('outdoor_running', 'Outdoor Running'),
        ('indoor_running', 'Indoor Running'),
        ('rope_jumping', 'Rope Jumping'),
        ('custom', 'Custom Cardio'),
    ]

    CALISTHENICS_TYPES = [
        ('push_ups', 'Push Ups'),
        ('crunches', 'Crunches'),
        ('pull_ups', 'Pull Ups'),
        ('chin_ups', 'Chin Ups'),
        ('custom', 'Custom Calisthenics'),
    ]

    WEIGHTLIFTING_TYPES = [
        ('upper_body', 'Upper Body'),
        ('lower_body', 'Lower Body'),
    ]

    UPPER_BODY_EXERCISES = [
        ('bench_press', 'Bench Press'),
        ('curls', 'Curls'),
        ('custom', 'Custom Upper Body'),
    ]

    LOWER_BODY_EXERCISES = [
        ('squats', 'Squats'),
        ('custom', 'Custom Lower Body'),
    ]

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    exercises = models.ManyToManyField(
        CustomExercise,
        through='WorkoutExercise',
        related_name='exercise_workouts'
        )

    

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
    