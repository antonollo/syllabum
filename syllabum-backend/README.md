# Syllabum (backend):

> Diz respeito ao backend da plataforma. A esquematização da API REST, serviços de regras de negócio e dados estão contidos neste repositório.

--- 

## Pré-requisitos:

Certifique-se de ter instalado:

- uv;
- Python 3.10+.

Para verificar se os pré-requisitos foram cumpridos, insira os seguintes comandos no terminal:

```text

uv --version            # uv 0.12.x
python --version        # Python 3.10+

```

Se os requisitos acima não foram cumpridos, por favor, confira os links a seguir para instalar esse material:

1. [Instalação do uv](https://docs.astral.sh/uv/getting-started/installation/);
2. [Instalação do Python 3.10+](https://www.python.org/downloads/release/python-3147/).

---

## Configurar e executando o Backend:

Com os pré-requisitos devidamente cumpridos, para configurar e utilizar o backend do Syllabum, basta inserir os seguintes comandos no terminal:

```text

uv sync                     # Instalação de dependências necessárias.
cd src/syllabum_backend     # Supondo que estamos no diretório-raiz.
uv run fastapi dev          # Inicialização do Backend (FastAPI).

```