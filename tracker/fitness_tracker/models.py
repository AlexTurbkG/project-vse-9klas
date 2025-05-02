from django.db import models

# Create your models here.
class Workout(models.Model):
    WORKOUT_TYPES = [
        ('cardio', 'Cardio'),
        ('weight strength', 'Weight Strength'),
        ('calisthenics', 'Calisthenics'),
        ('stretching', 'Stretching'),
    ]

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20,choices=WORKOUT_TYPES)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
