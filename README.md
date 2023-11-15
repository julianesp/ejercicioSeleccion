# Requerimientos

- Python=3.10.6
- virtualenv (pip install virtualenv)
- graphviz (https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224; https://gitlab.com/graphviz/graphviz/-/releases
  )
- SO: Windows

# 1. Backend

## 1.1 Entorno virtual

##### 1. Ingresar a la carpeta back

    cd back

##### 2. Crear entorno virtual

    virtualenv venv --python=python310

##### 3. Activar entorno virtual

    source venv/Scripts/activate

##### 4. Instalar librerias

    pip install -r requirements.txt

##### 5. Desactivar entorno virtual

    deactivate

## 1.2 Configurar base de datos

##### 1. Crear migración

    alembic revision --autogenerate -m "Initial migration"

##### 2. Ejecutar migraciones

    alembic upgrade head

##### 3. Crear base de datos

    python create_db.py

## 1.3 Iniciar servidor

    uvicorn main:app --reload

## 1.4 Conectarse a la base de datos mediante un gestor

1. Seleccionar SQLite
2. Path: back\test.db

## 1.5 Plus

##### 1. Generar archivos requirements.txt

    pip freeze > requirements.txt
