# PMT

## Overview
The **PMT** is a web-based application built with **FastAPI** that provides features for managing projects, tasks, and users with role-based permissions. The application is containerized using **Docker** and uses **PostgreSQL** as the database.

---

## Features
1. **Authentication**
   - Login with username and password to receive a JWT token.

2. **Role Management**
   - Define roles (Admin, Manager, User) to control access.

3. **User Management**
   - Add, update, delete, and list users.

4. **Task Management**
   - Create, update, delete, and assign tasks.
   - Manage task types and statuses.

5. **Security**
   - Passwords are hashed using `bcrypt`.
   - Role-based access control (RBAC).

---

## Technologies Used
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Authentication:** JWT
- **Containerization:** Docker & Docker Compose

---

## Project Structure
```plaintext
project-management-tool/
├── app/
│   ├── main.py
│   ├── models/
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── task.py
│   │   ├── task_status.py
│   │   └── task_type.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── task.py
│   │   ├── task_status.py
│   │   ├── task_type.py
│   │   └── auth.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── task.py
│   │   ├── task_status.py
│   │   └── task_type.py
│   ├── services/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── task.py
│   │   ├── task_status.py
│   │   └── task_type.py
│   ├── config.py
│   └── utils/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Installation

### Prerequisites
- **Docker** and **Docker Compose** installed on your system.
- Python 3.9+ (for local development).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Kaydhiman/pmt_backend.git
   cd project-management-tool
   ```

2. Create a `.env` file:
   ```plaintext
   DATABASE_URL=postgresql://postgres:password@db/project_management
   SECRET_KEY=your_secret_key_here
   ...
   ```
   Check example.env file for all the required variables

3. Build and start the services:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - API Documentation: `http://localhost:8000/docs`

---

## API Endpoints

### Authentication
- **POST** `/auth/login`: Login with username and password to get a JWT token.

### Users
- **GET** `/users`: List all users (Admin only).
- **POST** `/users`: Add a new user (Admin only).
- **PUT** `/users/{id}`: Update user information (Admin only).
- **DELETE** `/users/{id}`: Delete a user (Admin only).

### Roles
- **GET** `/roles`: List all roles (Admin only).
- **POST** `/roles`: Add a new role (Admin only).
- **PUT** `/roles/{id}`: Update role information (Admin only).
- **DELETE** `/roles/{id}`: Delete a role (Admin only).

### Tasks
- **GET** `/tasks`: List all tasks (Managers and Admins).
- **POST** `/tasks`: Add a new task (Managers only).
- **PUT** `/tasks/{id}`: Update task information (Managers only).
- **DELETE** `/tasks/{id}`: Delete a task (Managers only).

### Task Types and Statuses
- Similar CRUD endpoints for managing task types and statuses.

---

## Development

1. Activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Security Best Practices
1. Use a strong **SECRET_KEY**.
2. Store sensitive information like database credentials in a `.env` file.
3. Rotate JWT secrets periodically.
4. Regularly update dependencies.

---

## License
MIT License. Feel free to use and modify this project.

---

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

