
# Python API Template

[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.4-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat&logoColor=white&label=uv&color=yellow)](https://github.com/astral-sh/uv)
[![Postgres](https://img.shields.io/badge/Postgres-17-%23316192.svg?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![QDrant](https://img.shields.io/badge/Qdrant-1.12.5-red.svg?style=flat&logoColor=white)](https://www.postgresql.org/)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json&logoColor=white&labelColor=grey)](https://pydantic.dev)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.32.0-green?style=flat&logo=uvicorn&logoColor=white)](https://www.uvicorn.org/)
[![Langchain](https://img.shields.io/badge/Langchain-0.3.4-red?style=flat&logoColor=white)](https://www.langchain.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-0.0.22-violet?style=flat&logoColor=white)](https://sqlmodel.tiangolo.com/)


## Project description
This project is intended to be


## Install dependencies 

In order to run the project, you need to install _UV_ first.

On Linux and MacOS environments, launch the following command:

```shell
curl -LsSf https://astral.sh/uv/0.5.6/install.sh | sh
```

On Windows environments, launch the following command.

```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.5.6/install.ps1 | iex"
```

After _UV_ has been installed, you are ready to install project dependencies:

```shell
uv sync 
```

## Launching the application

To start the server, launch the following command:

```shell
python main.py
```

## Code quality

To perform code linting (e.g. remove unused dependencies and similar) launch the following command:
```shell
ruff check --fix
```

To format the code, launch the following command:

```shell
ruff format 
```

