# utils_tools

# Utils Tools

## Descripción

Utils Tools es un proyecto que proporciona una colección de herramientas y utilidades para facilitar diversas tareas. Este proyecto está construido con FastAPI y utiliza Poetry para la gestión de dependencias.

## Requisitos

- Python 3.8+
- Poetry

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tu_usuario/utils_tools.git
    cd utils_tools
    ```

2. Instala las dependencias usando Poetry:

    ```sh
    poetry install
    ```

3. Crea un archivo `.env` en la raíz del proyecto y añade las variables de entorno necesarias:

    ```env
    PROJECT_NAME=Utils Tools
    APP_VERSION=0.1.0
    APP_DOC_URL=/docs
    ```

## Uso

Para iniciar la aplicación, ejecuta el siguiente comando:

```sh
export PYTHONPATH=$PWD
poetry run python app/main.py
```