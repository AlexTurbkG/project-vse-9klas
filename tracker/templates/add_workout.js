document.addEventListener('DOMContentLoaded', function() {
    const workoutType = document.getElementById('id_type');
    const exerciseType = document.getElementById('id_exercise_type');
    const customExercise = document.getElementById('id_custom_exercise');
    
    workoutType.addEventListener('change', function() {
        fetch(`/get-exercise-types/?type=${this.value}`)
            .then(response => response.json())
            .then(data => {
                exerciseType.innerHTML = '<option value="">---------</option>' + 
                    data.choices.map(([value, label]) => 
                        `<option value="${value}">${label}</option>`
                    ).join('');
            });
    });

    // Trigger change event on page load if workout type is already selected
    if (workoutType.value) {
        workoutType.dispatchEvent(new Event('change'));
    }
});