This is a simple Library Management System built using Flask (Python framework) that allows users to manage books and members. It includes basic CRUD (Create, Read, Update, Delete) operations for both books and members.


Prerequisites:-
=============
Ensure you have the following installed:
Python 3.x
Flask

Steps to Run the Project:
=======================

1. cd library_management
2. python app.py
3. opren your browser and it goes to this port http://127.0.0.1:5000/



Design Choices:
===============
Flask Framework: Chosen for simplicity and easy integration with the front-end.
In-memory Data Storage: Data is stored in Python lists, suitable for prototyping but not persistent across restarts.
RESTful API: CRUD operations for books and members using Flask’s HTTP methods (GET, POST, PUT, DELETE).
HTML/CSS Interface: Basic, functional front-end without third-party libraries.
JavaScript: Used for dynamic updates (add, update, delete) without page reload.


Assumptions and Limitations:=
===========================
Assumptions:
============
In-memory storage: Data is lost on server restart. Persistent storage is needed for production.
No authentication: No user access control, anyone can modify data.
Basic front-end: Simple UI with minimal validation and error handling.

Limitations:
============
No persistent data storage: Data is lost on server restart.
Basic design: Limited responsiveness for mobile and minimal styling.
No error handling: Limited validation for API inputs.