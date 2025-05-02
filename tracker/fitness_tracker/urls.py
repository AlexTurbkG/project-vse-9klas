from django.urls import path
from .views import home, workouts

urlpatterns = [
    path('', home, name='home'),
    path('workouts/', workouts, name='workouts')
]