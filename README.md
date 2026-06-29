# App API 🚀

**App API** es una aplicación backend construida con **FastAPI** que implementa un sistema de control de acceso basado en roles (RBAC - Role-Based Access Control). La aplicación está completamente contenedorizada utilizando **Docker** y **Docker Compose**, utilizando **MySQL** como motor de base de datos.

---

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web para construir APIs con Python.
- **MySQL**: Base de datos relacional para el almacenamiento de información del sistema.
- **Docker & Docker Compose**: Para la contenedorización y despliegue rápido.
- **Pydantic**: Para la validación de esquemas y datos de entrada/salida.
- **JWT (JSON Web Tokens)**: Para la autenticación de usuarios y gestión de sesiones seguras.
- **Bcrypt**: Para el cifrado seguro de contraseñas.

---

## 📁 Estructura del Proyecto

El proyecto sigue una estructura limpia y modular:

- `src/app/core/`: Configuraciones de seguridad, cifrado de contraseñas y generación de tokens de acceso.
- `src/app/database/`: Utilidades y gestor de conexión para la base de datos.
- `src/app/module/`: Capa lógica de negocio separada por módulos del sistema (usuarios, roles, permisos y autenticación).
- `src/app/routers/`: Definición de los endpoints y controladores de la API.
- `src/app/scheme/`: Modelos de validación de datos (schemas) con Pydantic.

---

## 🔒 Control de Acceso basado en Roles (RBAC)

La API cuenta con seguridad por token JWT y un middleware que valida si el usuario cuenta con los permisos necesarios para realizar acciones específicas. El flujo general es:

1. El usuario inicia sesión y obtiene un token de acceso JWT.
2. El cliente envía el token en la cabecera de las peticiones protegidas.
3. El servidor decodifica el token, obtiene la identidad del usuario y verifica en la base de datos si su rol cuenta con los permisos correspondientes.
4. Si tiene el permiso requerido, la petición se procesa; de lo contrario, se retorna un error `403 Forbidden`.

---

## 🚀 Instalación y Despliegue con Docker

### Requisitos Previos
- **Docker** y **Docker Compose** instalados en el sistema.

### Paso 1: Configurar el archivo de Entorno
Crea un archivo `.env` en la raíz del proyecto para definir las configuraciones básicas (nombre de la app, credenciales de base de datos y llaves de seguridad).

### Paso 2: Iniciar la Aplicación
Ejecuta el siguiente comando en la terminal para compilar la imagen y levantar los contenedores de la API y de la base de datos:
```bash
docker-compose up --build
```

Esto levantará los servicios expuestos en sus puertos correspondientes para su consumo inmediato.

### Paso 3: Documentación Interactiva
Una vez corriendo el servidor, puedes explorar y probar todos los endpoints disponibles accediendo a la documentación autogenerada de Swagger UI:
👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 📌 Módulos de la API

La API organiza sus operaciones en los siguientes módulos principales:

- **Autenticación (`/auth`)**: Gestión de inicio de sesión y generación de tokens JWT.
- **Usuarios**: Endpoints para crear, consultar, actualizar y eliminar usuarios del sistema.
- **Roles**: Creación, actualización y eliminación de los roles del sistema.
- **Permisos**: Administración de permisos individuales y su asignación a los diferentes roles.
