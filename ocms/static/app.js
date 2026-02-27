const API = "http://127.0.0.1:8000/api";

// LOGIN
function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch(`${API}/auth/login/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    })
    .then(res => res.json())
    .then(data => {
        if (data.access) {
            localStorage.setItem("token", data.access);
            window.location.href = "/courses-page/";
        } else {
            document.getElementById("error").innerText =
                data.detail || "Invalid credentials";
        }
    });
}

// LOAD COURSES
function loadCourses() {
    fetch(`${API}/courses/`)
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("courseList");
        container.innerHTML = "";

        data.forEach(course => {
            container.innerHTML += `
                <div class="card">
                    <h4>${course.title}</h4>
                    <p>${course.description || ""}</p>
                    <button onclick="enroll(${course.id})">
                        Enroll
                    </button>
                </div>
            `;
        });
    });
}

// ENROLL
function enroll(courseId) {
    const token = localStorage.getItem("token");

    fetch(`${API}/enroll/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({course: courseId})
    })
    .then(res => res.json())
    .then(data => {
        alert(data.detail || "Enrolled!");
    });
}

// LOGOUT
function logout() {
    localStorage.removeItem("token");
    window.location.href = "/";
}