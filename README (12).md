# API de Estudiantes con FastAPI 🚀

## ¿Qué es este proyecto?

Este proyecto es una API desarrollada con FastAPI que permite gestionar estudiantes de un programa académico.

La API permite:

- Consultar estudiantes
- Buscar estudiantes por ID
- Crear nuevos estudiantes
- Filtrar estudiantes activos o inactivos

---

# Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic

---

# Instalación del proyecto

## 1. Instalar Python

Descargar Python desde:

https://www.python.org/downloads/

Durante la instalación es importante marcar:

```text
Add Python to PATH
```

---

# Crear el proyecto

## 1. Crear carpeta del proyecto

```text
student-card-api
```

---

## 2. Abrir el proyecto en VS Code

En Visual Studio Code:

```text
File > Open Folder
```

Seleccionar la carpeta del proyecto.

---

# Crear entorno virtual

## ¿Qué es venv?

`venv` sirve para crear un entorno virtual en Python.

Permite instalar librerías sin afectar otros proyectos.

---

## Crear entorno virtual

En la terminal ejecutar:

```bash
python -m venv .venv
```

---

# Activar entorno virtual

## En Windows

```bash
.\.venv\Scripts\activate
```

---

# Instalar dependencias

```bash
pip install fastapi uvicorn pydantic email-validator
```

---

# Explicación de dependencias

| Dependencia | Función |
|---|---|
| FastAPI | Framework para crear APIs |
| Uvicorn | Servidor que ejecuta la API |
| Pydantic | Validación de datos |
| email-validator | Validación de correos |

---

# Ejecutar la API

```bash
uvicorn main:app --reload
```

---

# Abrir documentación

```text
http://127.0.0.1:8000/docs
```

---

# Explicación del main.py

## Importaciones

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
```

Estas líneas importan herramientas necesarias para la API.

---

# Crear la aplicación

```python
app = FastAPI(
    title="API de Estudiantes",
    description="Una API para gestionar estudiantes",
    version="1.0.0"
)
```

---

# Modelos

## Modelo Student

```python
class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    program: str
    active: bool
```

Define cómo debe verse un estudiante.

---

## Modelo StudentCreate

```python
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    program: str
    active: bool
```

Sirve para crear estudiantes nuevos.

---

# Base de datos en memoria

```python
students = [
```

Es una lista temporal donde se almacenan estudiantes.

---

# Endpoint GET

```python
@app.get("/students")
```

Obtiene estudiantes.

---

# Endpoint POST

```python
@app.post("/students")
```

Crea estudiantes nuevos.

---

# Ejemplo JSON

```json
{
  "name": "Nicol",
  "email": "nicol@email.com",
  "program": "Software",
  "active": true
}
```

---

# ¿Qué es HTTP?

HTTP es el protocolo que permite la comunicación entre cliente y servidor.

---

# Diferencia entre GET y POST

| Método | Función |
|---|---|
| GET | Obtener información |
| POST | Crear información |

---

# ¿Qué es serializar?

Serializar es convertir datos de Python a JSON para poder enviarlos por internet.

---

# ¿Qué es una path operation?

Es una ruta de la API que realiza una acción específica.

Ejemplo:

```python
@app.get("/students")
```

---

# Conclusión

Este proyecto permite comprender el funcionamiento básico de una API REST utilizando FastAPI.
