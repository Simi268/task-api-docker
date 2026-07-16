from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from repository import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task,
)

app = FastAPI(
    title="Task API",
    description="Task Management API using FastAPI and PostgreSQL",
    version="2.0.0"
)


# ----------------------------
# Pydantic Models
# ----------------------------

class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


# ----------------------------
# Root Endpoint
# ----------------------------

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "2.0",
        "database": "PostgreSQL"
    }


# ----------------------------
# Health Check
# ----------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# ----------------------------
# Get All Tasks
# ----------------------------

@app.get("/tasks")
def read_tasks():
    return get_all_tasks()


# ----------------------------
# Get Task By ID
# ----------------------------

@app.get("/tasks/{task_id}")
def read_task(task_id: int):

    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return task


# ----------------------------
# Create Task
# ----------------------------

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def add_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    return create_task(task.title)


# ----------------------------
# Update Task
# ----------------------------

@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    updated = update_task(
        task_id,
        task.title,
        task.done
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    return updated


# ----------------------------
# Delete Task
# ----------------------------

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(task_id: int):

    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )