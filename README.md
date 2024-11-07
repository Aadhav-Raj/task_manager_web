Task Manager Django Backend
This is the backend for a Task Manager Android app, built using Django. It provides user authentication, token-based authorization, email verification, and CRUD operations for managing tasks. The backend uses SQLite as the database and integrates with Gmail SMTP for email verification.

Features:
User Authentication: Allows users to register, log in, and manage their profiles.
Email Verification: Uses Gmail SMTP integration to send verification emails with links for confirming user accounts.
Token Authorization: Implements token-based authentication for secure API access.
CRUD Operations: Users can create, read, update, and delete tasks.
SQLite Database: Utilizes SQLite for storing user and task data.

The Django server serves as a backend for the android app developed by Kotlin  under the link https://github.com/Aadhav-Raj/task_manager_app
Requirements:
Python 3.x
Django
Django REST Framework
SQLite (default database)
