from django.urls import path
from .views import home, add_workout, del_workout, edit_workout

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_workout, name='add_workout'),
    path('delete/<int:workout_id>/', del_workout, name='del_workout'),
    path('edit/<int:workout_id>/', edit_workout, name ='edit_workout'),
]