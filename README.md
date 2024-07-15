# Projeto FastAPI para o bootcamp da DIO
projeto_fastapi_dio/
├── projeto_fastapi_dio/
│   ├── __init__.py
│   ├── controller.py
│   ├── models.py
│   ├── exceptions.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_controller.py
├── pyproject.toml
└── README.md

# Objetivo
Este é um projeto de exemplo para criar e atualizar produtos com tratamento de exceções.

## Configuração do Ambiente
1. Instalar [Pyenv](https://github.com/pyenv/pyenv#installation).
2. Instalar [Poetry](https://python-poetry.org/docs/#installation).

Após criar todos os arquivos, você pode configurar o ambiente e instalar as dependências:

```bash
# Instalar dependências do projeto
poetry install

# Executar os testes para garantir que tudo está funcionando corretamente
poetry run pytest