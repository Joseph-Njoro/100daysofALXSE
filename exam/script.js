document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    // Implement login functionality here
    // Example: Send username and password to server for authentication

    // Dummy data for demonstration
    const user = {
        username: "student1",
        schedules: [
            { subject: "Math", date: "2024-05-10", time: "09:00", duration: "2 hours" },
            { subject: "Science", date: "2024-05-15", time: "13:30", duration: "2.5 hours" }
        ]
    };

    displaySchedule(user);
});

function displaySchedule(user) {
    const scheduleDiv = document.getElementById("schedule");
    scheduleDiv.innerHTML = "<h2>Schedule</h2>";
    if (user.schedules.length === 0) {
        scheduleDiv.innerHTML += "<p>No exams scheduled.</p>";
    } else {
        user.schedules.forEach(function(exam) {
            scheduleDiv.innerHTML += `<p>${exam.subject} - Date: ${exam.date}, Time: ${exam.time}, Duration: ${exam.duration}</p>`;
        });
    }
}