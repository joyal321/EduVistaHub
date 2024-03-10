const courseList = document.getElementById('course-list');
const courseTitle = document.getElementById('course-title');
const courseDescription = document.getElementById('course-description');

courseList.addEventListener('click', (event) => {
    if (event.target.tagName.toLowerCase() === 'li') {
        const courseId = event.target.getAttribute('data-id');
        fetch(`py_full.json?id=${courseId}`)
            .then((response) => response.json())
            .then((course) => {
                courseTitle.textContent = course.title;
                courseDescription.textContent = course.description;
            });
    }
});