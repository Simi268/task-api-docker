# Task API

A RESTful Task Management API built with **FastAPI**, **PostgreSQL**, and **Docker Compose**.

## Features

- Create, Read, Update and Delete tasks
- PostgreSQL database
- Repository Pattern architecture
- Input validation using Pydantic
- Swagger API documentation
- Dockerized application

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- Psycopg
- Pydantic

---

## Project Structure

```text
task-api-docker/
│── main.py
│── repository.py
│── database.py
│── schema.sql
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── .env.example
│── README.md

```

---

## Setup

Clone the repository:

```bash
git clone https://github.com/Simi268/task-api-docker.git
cd task-api-docker
```

Create a `.env` file using `.env.example`.

Start the application:

```bash
docker compose up --build
```

Open:

```
http://localhost:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Information |
| GET | `/health` | Health Check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

---

## Architecture

The project follows the **Repository Pattern**.

```
FastAPI Routes
        │
        ▼
 Repository Layer
        │
        ▼
 PostgreSQL Database
```

This keeps the API routes separate from the database logic and allows changing the storage implementation without modifying the API endpoints.

---

## Persistence

Data is stored in a Docker volume.

Persistence was verified by:

1. Creating a task.
2. Running:

```bash
docker compose down
docker compose up
```

3. Verifying that the task still exists in the database.

---

