from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI(
    title="API de Estudiantes",
    description="Una API para gestionar estudiantes en un programa académico",
    version="1.0.0"

)

# =========================
# MODELOS
# =========================

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    program: str
    active: bool


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    program: str
    active: bool


# =========================
# BASE DE DATOS EN MEMORIA
# =========================

students = [
    {
        "id": 1,
        "name": "Sandra Lopez",
        "email": "sandra.lopez@email.com",
        "program": "Análisis y Desarrollo de Software",
        "active": True
    },
    {
        "id": 2,
        "name": "Alberto Manrique",
        "email": "alberto123m@email.com",
        "program": "Producción Multimedia",
        "active": False
    },
    {
        "id": 3,
        "name": "Andrea Lopez",
        "email": "andreita.lopez@email.com",
        "program": "Análisis y Desarrollo de Software",
        "active": True
    },
    {
        "id": 4,
        "name": "Eliecer Galindo",
        "email": "eliecer.galindo@email.com",
        "program": "Producción Multimedia",
        "active": False
    },
    {
        "id": 5,
        "name": "Martha Quitian",
        "email": "marthaQ@email.com",
        "program": "Medios Audiovisuales",
        "active": False
    }
    
]


# =========================
# GET /students/{id}
# =========================

@app.get("/students/{id}", response_model=Student)
def get_student(id: int):

    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# =========================
# POST /students
# =========================

@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):

    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "email": student.email,
        "program": student.program,
        "active": student.active
    }

    students.append(new_student)

    return new_student


# =========================
# GET /students?active=true
# =========================

@app.get("/students", response_model=List[Student])
def get_students(active: Optional[bool] = None):

    if active is None:
        return students

    filtered_students = []

    for student in students:
        if student["active"] == active:
            filtered_students.append(student)

    return filtered_students