from django.urls import path
from .views import home, add_workout, del_workout, edit_workout, add_exercise, workout_details, delete_exercise, manage_exercises
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_workout, name='add_workout'),
    path('delete/<int:workout_id>/', del_workout, name='del_workout'),
    path('edit/<int:workout_id>/', edit_workout, name ='edit_workout'),
    path('add-exercise/', add_exercise, name='add_exercise'),
    path('workout/<int:workout_id>/', workout_details, name='workout_details'),
    path('delete-exercise/<int:exercise_id>/', delete_exercise, name='delete_exercise'),
    path('manage-exercises/', manage_exercises, name='manage_exercises'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)