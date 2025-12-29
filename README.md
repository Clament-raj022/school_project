School Management System (Django)
A School Management System built using Django, designed to manage students, teachers, and administrators with role-based access control.
Each user role has specific permissions to ensure secure and organized data handling.
📌 Project Overview
This project helps in managing school operations digitally by providing separate access for:
Students – View personal profile and marks
Teachers – Manage student marks and view student list
Admin – Manage the entire system (students & teachers)
🧩 Apps Included
App Name              Description
Student              Student profile and marks viewing
Teacher              Student list management and marks update
Admin                Full control over students and teachers
👥 User Roles & Permissions
👨‍🎓 Student
View own profile
View marks
No permission to edit data
👩‍🏫 Teacher
View list of students
Update student marks
View own profile
🛠️ Admin
Add / update / delete students
Add / update / delete teachers
Manage entire database
Full system access
✨ Key Features
Role-based authentication
Secure login system
Separate dashboards for Student, Teacher, and Admin
CRUD operations for admin
Marks management by teachers
Clean and scalable Django project structure
🛠️ Technologies Used
Backend: Python, Django
Database: SQLite (can be changed to MySQL / PostgreSQL)
Frontend: HTML, CSS, Bootstrap
Authentication: Django built-in authentication system
📂 Project Structure
school/
│
├── student/
├── teacher/
├── admin_app/
├── templates/
├── static/
├── manage.py
└── db.sqlite3
