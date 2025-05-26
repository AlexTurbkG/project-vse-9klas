from django import forms
from .models import Workout, CustomExercise, WorkoutExercise


class CustomExerciseForm(forms.ModelForm):
    class Meta:
        model = CustomExercise
        fields = ['name', 'category']
        widgets = {
            'category': forms.Select(choices=CustomExercise.CATEGORY_TYPES)
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if CustomExercise.objects.filter(name__iexact = name).exists():
            raise forms.ValidationError('An exercise with this name already exists.')
        return name
    

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'type', 'duration_minutes', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        workout_type = cleaned_data.get('type')
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