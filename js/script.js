// Welcome message
function welcomeMessage() {
    alert("Welcome to Student Management System!");
}


// Open student message
function showMessage() {
    alert("Opening student records...");
}


// -------------------------
// ADD STUDENT
// -------------------------

function addStudent() {

    let id = document.getElementById("studentId").value;
    let name = document.getElementById("studentName").value;
    let course = document.getElementById("studentCourse").value;
    let year = document.getElementById("studentYear").value;

    if (id == "" || name == "" || course == "" || year == "") {
        alert("Please fill all student details!");
        return;
    }

    let table = document.getElementById("studentTable");

    let row = table.insertRow();

    row.insertCell(0).innerHTML = id;
    row.insertCell(1).innerHTML = name;
    row.insertCell(2).innerHTML = course;
    row.insertCell(3).innerHTML = year;

    alert("Student added successfully!");

    document.getElementById("studentId").value = "";
    document.getElementById("studentName").value = "";
    document.getElementById("studentCourse").value = "";
    document.getElementById("studentYear").value = "";
}


// -------------------------
// SEARCH STUDENT
// -------------------------

function searchStudent() {

    let input = document
        .getElementById("searchInput")
        .value
        .toLowerCase();

    let table = document.getElementById("studentTable");

    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {

        let name = rows[i].getElementsByTagName("td")[1];

        if (name) {

            let text = name.textContent.toLowerCase();

            if (text.includes(input)) {
                rows[i].style.display = "";
            }
            else {
                rows[i].style.display = "none";
            }
        }
    }
}


// -------------------------
// ADD COURSE
// -------------------------

function addCourse() {

    let id = document.getElementById("courseId").value;
    let name = document.getElementById("courseName").value;
    let duration = document.getElementById("courseDuration").value;

    if (id == "" || name == "" || duration == "") {
        alert("Please fill all course details!");
        return;
    }

    let table = document.getElementById("courseTable");

    let row = table.insertRow();

    row.insertCell(0).innerHTML = id;
    row.insertCell(1).innerHTML = name;
    row.insertCell(2).innerHTML = duration;

    alert("Course added successfully!");

    document.getElementById("courseId").value = "";
    document.getElementById("courseName").value = "";
    document.getElementById("courseDuration").value = "";
}


// -------------------------
// ADD TEACHER
// -------------------------

function addTeacher() {

    let id = document.getElementById("teacherId").value;
    let name = document.getElementById("teacherName").value;
    let department = document.getElementById("teacherDepartment").value;
    let subject = document.getElementById("teacherSubject").value;

    if (
        id == "" ||
        name == "" ||
        department == "" ||
        subject == ""
    ) {
        alert("Please fill all teacher details!");
        return;
    }

    let table = document.getElementById("teacherTable");

    let row = table.insertRow();

    row.insertCell(0).innerHTML = id;
    row.insertCell(1).innerHTML = name;
    row.insertCell(2).innerHTML = department;
    row.insertCell(3).innerHTML = subject;

    alert("Teacher added successfully!");

    document.getElementById("teacherId").value = "";
    document.getElementById("teacherName").value = "";
    document.getElementById("teacherDepartment").value = "";
    document.getElementById("teacherSubject").value = "";
}