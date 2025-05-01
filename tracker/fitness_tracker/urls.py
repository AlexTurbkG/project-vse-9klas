from django.urls import path
from .views import home, WorkoutList

urlpatterns = [
    path('', home, name='home'),
    path('workouts/', WorkoutList.as_view(), name='workout-list')
]