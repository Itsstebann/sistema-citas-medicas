# Sistema de Citas Médicas

API REST para gestión de citas médicas construida con FastAPI y PostgreSQL.

## Tecnologías
- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic

## Instalación

1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `venv\Scripts\activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Configurar variables de entorno en `.env`
6. Correr migraciones: `alembic upgrade head`
7. Iniciar servidor: `uvicorn main:app --reload`

## Endpoints

### Autenticación
- `POST /auth/registro` — registrar usuario
- `POST /auth/login` — iniciar sesión

### Pacientes
- `POST /pacientes` — registrar paciente
- `GET /pacientes` — listar pacientes
- `GET /pacientes/{id}` — obtener paciente

### Doctores
- `POST /doctores` — registrar doctor
- `GET /doctores` — listar doctores
- `GET /doctores/{id}` — obtener doctor

### Citas
- `POST /citas` — agendar cita
- `GET /citas` — listar citas
- `GET /citas/{id}` — obtener cita
- `PATCH /citas/{id}/estado` — actualizar estado