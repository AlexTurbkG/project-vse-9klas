from django import forms
from .models import Workout, CustomExercise, WorkoutExercise


class CustomExerciseForm(forms.ModelForm):
    class Meta:
        model = CustomExercise
        fields = ['name', 'category']
        widgets = {
            'category': forms.Select(choices=CustomExercise.CATEGORY_TYPES)
        }

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'type', 'exercise_type', 'duration_minutes', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['exercise_type'].widget = forms.Select(choices=[])

    def clean(self):
        cleaned_data = super().clean()
        workout_type = cleaned_data.get('type')
        exercise_type = cleaned_data.get('exercise_type')
        return cleaned_data

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'reps', 'weight']

WorkoutExerciseFormSet = forms.inlineformset_factory(
    Workout, WorkoutExercise,
    form=WorkoutExerciseForm,
    extra=1,
    can_delete=True
)