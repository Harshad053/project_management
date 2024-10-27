# Project Management API


A Django REST framework API for managing clients, projects, and users, with capabilities to assign
users to projects, view assigned projects for logged-in users, and perform CRUD operations for
clients and projects.

## Table of Contents

1. Features
2. Requirements
3. Installation
4. Usage
5. API Endpoints
6. Database Configuration
7. Contributing


## Features

- Client Management: Create, retrieve, update, and delete client information.
- Project Assignment: Add projects for clients and assign users to them.
- User Assigned Projects: Retrieve projects assigned to the logged-in user.


## Requirements

- Python 3.x
- Django 3.x or later
- Django REST Framework
- MySQL (or PostgreSQL)

## Installation

1. Clone the Repository
 git clone https://github.com/Harshad053/project_management.git
 cd project_management

3. Create a Virtual Environment and Install Dependencies
 python -m venv venv
 source venv/bin/activate # On Mac/Linux
 venv\Scripts\activate # On Windows
 pip install -r requirements.txt

3. Set Up Environment Variables
Create a .env file in the project root with the following settings:
 SECRET_KEY='your-secret-key'
 DATABASE_NAME='your_db_name'
 DATABASE_USER='your_db_user'
 DATABASE_PASSWORD='your_db_password'
 DATABASE_HOST='localhost' # Or the IP address of your database server
 DATABASE_PORT='3306' # Default for MySQL, use 5432 for PostgreSQL

4. Apply Database Migrations
 python manage.py migrate

6. Create a Superuser for Admin Access
 python manage.py createsuperuser

8. Run the Development Server
 python manage.py runserver
Your project will be accessible at http://127.0.0.1:8000


## Usage
- Admin Access: Access the Django admin dashboard at http://127.0.0.1:8000/admin to manage
users and view registered clients and projects.
- API Testing: You can use tools like Postman or curl to interact with the API endpoints described
below


## API Endpoints
### Client Endpoints

- List all clients
 - Request: GET /api/clients/
- Create a new client
 - Request: POST /api/clients/
 - Input:
 {'client_name' : 'Company A'}
- Retrieve client details
 - Request: GET /api/clients/<id>/


### Project Endpoints

- Create a new project
 - Request: POST /api/projects/create/
 - Input:
 {'project_name' : 'Project A', 'client' : 1, 'users' : [1]}

## Database Configuration

This project uses MySQL (or PostgreSQL if configured). Update database settings in .env as shown
in the Installation section.
For MySQL, run these commands to set up your database:
 CREATE DATABASE project_management_db;
 CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password'


 GRANT ALL PRIVILEGES ON project_management_db.* TO 'your_db_user'@'localhost';
 FLUSH PRIVILEGES;
## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -am 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a Pull Request.

