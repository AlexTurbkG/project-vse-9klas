from django.urls import path
from .views import home, add_workout
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('add_workout/', add_workout, name='add_workout'),
    path('delete/<int:workout_id>/', views.del_workout, name='del_workout'),
]