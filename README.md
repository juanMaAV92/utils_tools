# Utils Tools

## Descripción

Utils Tools es una solución integral diseñada para proporcionar una colección de herramientas y utilidades avanzadas para la manipulación de archivos. Desarrollado con FastAPI y gestionado mediante Poetry, este proyecto tiene como objetivo ofrecer un servicio seguro y eficiente para la manipulación de archivos, eliminando la necesidad de subir documentos sensibles a plataformas externas y mitigando así los riesgos de seguridad asociados.

## Requisitos

- Python 3.10+
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

1. Inicia el servidor:

    ```sh
    export PYTHONPATH=$PWD
    poetry run python app/main.py
    ```

2. Accede a la documentación interactiva de la API en [http://localhost:8000/docs](http://localhost:8000/docs).

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:

```sh
poetry run pytest
```

Para formatar el código, usa el siguiente comando:

```sh
poetry run black .
```

Para ordenar las importaciones, usa el siguiente comando:

```sh
poetry run isort .
```

Para ejecutar flake8, usa el siguiente comando:

```sh
poetry run flake8
```

## Licencia

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

Distribuido bajo la licencia MIT. Consulte [LICENSE](LICENSE) para obtener más información.