# YGMotors

Trabalho de reposição da primeira etapa do Tech Challenge FIAP.

---

## Sumário

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Pré-requisitos](#pré-requisitos)
4. [Como Executar Localmente](#como-executar-localmente)
5. [Documentação e Acesso](#documentação-e-acesso)
6. [Autores](#autores)

---

## Sobre o Projeto

# YG Motors API  
API desenvolvida em **FastAPI** utilizando arquitetura **Hexagonal**, 
com **SQLAlchemy**, **Alembic** para migrations e **PostgreSQL** para o banco de dados.

---

## Tecnologias Utilizadas

- **Python** (Fast API): Framework para construção de aplicações em python com performance e simplicidade.
- **Docker**: Ferramenta de containerização para garantir a portabilidade e consistência do ambiente.
- **PostgreSQL**: Banco de dados relacional utilizado para persistência de dados.
- **Alembic**: Ferramenta para versionar as alterações no banco de dados
- **Arquitetura Hexagonal**: Padrão arquitetural focado em modularidade e independência de tecnologias externas.
- **Swagger/OpenAPI**: Ferramenta para documentação interativa e testes das APIs.

---

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em seu ambiente:

- **Docker**: Para construir as imagens da aplicação.
- **Git**: Para clonar o repositório.
- **Python + venv**: Para rodar localmente

---

## Como Executar Localmente com Docker

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

1. **Clonar o repositório**
   ```bash
   git clone git@github.com:YanGianini/YGMotors.git
   cd YGMotors
   ```

2. **Criar arquivo .env baseado em .env-example**
    ### Exemplo:
    # APP
    APP_ENV=development
    APP_NAME=vehicle_api

    # DATABASE
    DB_HOST=db
    DB_PORT=5432
    DB_NAME=ygm_db
    DB_USER=postgres
    DB_PASSWORD=postgres

    # SQLAlchemy
    DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/ygm_db

3. **Rodar o banco de dados e api com Docker Compose, aplicar migrações do alembic**
   ```bash
   docker compose up --build
   ```
   ou
      ```bash
   make build
   ```

  para continuar rodando o projeto é possivel utilizar tanto o "docker compose up" ou "make run"

4. **Adicionar migração Alembic**

  ### Adicionar import do ModelORM adicionado ao arquivo alembic/versions/env.py
  ### No shell do container rodar
   ```bash
   alembic revision --autogenerate -m "seu texto descritivo da migração"
   ```

  caso seja apenas uma alteração basta rodar o comando acima.
---

## Documentação e Acesso

- **Swagger UI**: Acesse a interface interativa da API no seguinte
  link: [http://localhost:8000/docs](http://localhost:8000/docs).

- **Coleção Postman**: Utilize a coleção disponível em [
  `docs/YGMotors.postman_collection.json`](./docs/YGMotors.postman_collection.json) 

- **Event Storming**: Visualize no arquivo [`docs/YGMortorsEventStorm.pdf`](./docs/YGMortorsEventStorm.pdf) o processo de *Event Storming* utilizado no projeto.


- **Descrição do Problema**: Consulte os documentos para entender os requisitos e o contexto do projeto.
  - Fase 1: [`docs/Fase 1 - Trabalho Reposição Tech Challenge SOAT.pdf`](./docs/Fase 1 - Trabalho Reposição Tech Challenge SOAT.pdf)

<!-- - **Documentações e Diagramas - **: Consulte o documento [`docs/finalizar diagrama`](./docs/finalizar diagrama) para entender os requisitos e contexto do projeto -->

---

## Participante

- **Yan Gianini - RM358368**  
  *Discord*: @.gianini | E-mail: yangianini@gmail.com