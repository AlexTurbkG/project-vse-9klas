from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        workout = Workout
        fields = ['cardio','weight strenght', 'calisthenics', 'stetching']
        