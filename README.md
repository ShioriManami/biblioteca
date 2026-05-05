# Biblioteca — Sistema de gestion de biblioteca con Django

Aplicacion web para la gestion de una biblioteca desarrollada con **Django**, con modulos para usuarios, administradores y manejo de direcciones. Incluye panel de administracion integrado y sistema de migraciones.

---

## Caracteristicas

- Registro y gestion de usuarios
- Panel de administracion (admin Django personalizado)
- Manejo de direcciones vinculadas a usuarios
- Sistema de formularios con validacion
- Migraciones de base de datos versionadas
- Soporte para Bootstrap (via Popper.js)

---

## Stack tecnico

| Tecnologia | Uso |
|---|---|
| Python | Lenguaje principal |
| Django | Framework web |
| SQLite | Base de datos (por defecto) |
| Bootstrap + Popper.js | Estilos y componentes UI |
| HTML/CSS | Plantillas del frontend |

---

## Estructura del proyecto

```
biblioteca/
├── manage.py                  # CLI de Django
├── biblioteca/                # Configuracion principal
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── apps/
    ├── Administrador/         # Modulo de administracion
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   └── urls.py
    ├── usuario/               # Gestion de usuarios
    │   ├── models.py          # Modelo Usuario con 10 migraciones
    │   ├── views.py
    │   ├── forms.py
    │   └── urls.py
    └── direccion/             # Modelo de direcciones
        ├── models.py          # Campos: calle, numero
        └── admin.py
```

---

## Inicio rapido

### Prerequisitos

- Python 3.10+
- pip

### Instalacion

```bash
git clone https://github.com/ShioriManami/biblioteca.git
cd biblioteca

# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install django

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario (acceso al admin)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
# Abre http://localhost:8000
```

### Panel de administracion

```
http://localhost:8000/admin
```

---

## Conceptos demostrados

- **Django ORM** — modelos relacionales con migraciones versionadas
- **Django Admin** — panel administrativo personalizado
- **Arquitectura MVT** (Model-View-Template) de Django
- **Formularios Django** — validacion server-side
- **Modular por apps** — separacion de responsabilidades
- **WSGI/ASGI** — soporte para despliegue en produccion