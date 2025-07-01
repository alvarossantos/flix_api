# Flix API

![Django REST Framework](https://img.shields.io/badge/Django%20REST-Framework-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎬 Sobre o Projeto

A **Flix API** é o backend para uma aplicação de catálogo de filmes, construída com Django e Django REST Framework. Ela fornece todos os endpoints necessários para gerenciar filmes, gêneros, atores e avaliações de usuários.

Esta API foi projetada para ser consumida por um frontend, e um exemplo de implementação pode ser encontrado no projeto [Streamlit Flix](https://github.com/alvarossantos/streamlit_flix_api), que utiliza esta API para criar uma interface de usuário interativa.

---

## ✨ Funcionalidades Principais

- **Autenticação de Usuário**: Sistema seguro de login baseado em token.
- **Gerenciamento de Filmes**: Operações de CRUD (Criar, Ler, Atualizar, Deletar) para filmes.
- **Gerenciamento de Gêneros**: CRUD completo para categorias de filmes.
- **Gerenciamento de Atores**: CRUD para informações dos atores.
- **Sistema de Avaliação**: Usuários autenticados podem avaliar os filmes.
- **Permissões Flexíveis**: Apenas administradores podem adicionar/modificar/deletar gêneros e atores, enquanto usuários autenticados podem registrar e gerenciar suas próprias avaliações.

---

## 🚀 Começando

Siga estas instruções para ter uma cópia do projeto rodando na sua máquina local para desenvolvimento e testes.

### Pré-requisitos

- Python 3.9 ou superior
- Pip (gerenciador de pacotes do Python)
- Git

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone [https://github.com/alvarossantos/flix_api.git](https://github.com/alvarossantos/flix_api.git)
   cd flix_api
   ```
2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No macOS/Linux
   source venv/bin/activate
   ```
3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure o banco de dados:**
   Execute as migrações para criar os modelos no seu banco de dados.

   ```bash
   python manage.py migrate
   ```
5. **Crie um superusuário:**
   Isso é necessário para acessar o painel de administração do Django.

   ```bash
   python manage.py createsuperuser
   ```
6. **(Opcional) Importe os dados iniciais:**
   O projeto inclui um comando para popular o banco de dados com dados de atores a partir de um arquivo `actors.csv`.

   ```bash
   python manage.py import_actors
   ```
7. **Rode o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   A API estará disponível em `http://127.0.0.1:8000/`.

---

## Endpoints da API

A URL base para os endpoints é `/api/v1/`.

### Autenticação

- `POST /api/v1/auth/token/`
  - **Descrição**: Autentica um usuário e retorna um token de acesso.
  - **Corpo da Requisição**: `{ "username": "seu_usuario", "password": "sua_senha" }`

### Gêneros

- `GET /api/v1/genres/`
  - **Descrição**: Lista todos os gêneros.
  - **Permissão**: Aberto.
- `POST /api/v1/genres/`
  - **Descrição**: Cria um novo gênero.
  - **Permissão**: Apenas Admin.
- `GET /api/v1/genres/<id>/`
  - **Descrição**: Obtém os detalhes de um gênero específico.
  - **Permissão**: Aberto.
- `PUT /api/v1/genres/<id>/`
  - **Descrição**: Atualiza um gênero.
  - **Permissão**: Apenas Admin.
- `DELETE /api/v1/genres/<id>/`
  - **Descrição**: Deleta um gênero.
  - **Permissão**: Apenas Admin.

### Atores

- `GET /api/v1/actors/`
  - **Descrição**: Lista todos os atores.
  - **Permissão**: Aberto.
- `POST /api/v1/actors/`
  - **Descrição**: Cria um novo ator.
  - **Permissão**: Apenas Admin.
- `GET /api/v1/actors/<id>/`
  - **Descrição**: Obtém os detalhes de um ator específico.
  - **Permissão**: Aberto.
- `PUT /api/v1/actors/<id>/`
  - **Descrição**: Atualiza um ator.
  - **Permissão**: Apenas Admin.
- `DELETE /api/v1/actors/<id>/`
  - **Descrição**: Deleta um ator.
  - **Permissão**: Apenas Admin.

### Filmes

- `GET /api/v1/movies/`
  - **Descrição**: Lista todos os filmes.
  - **Permissão**: Aberto.
- `POST /api/v1/movies/`
  - **Descrição**: Cria um novo filme.
  - **Permissão**: Apenas Admin.
- `GET /api/v1/movies/<id>/`
  - **Descrição**: Obtém os detalhes de um filme específico.
  - **Permissão**: Aberto.
- `PUT /api/v1/movies/<id>/`
  - **Descrição**: Atualiza um filme.
  - **Permissão**: Apenas Admin.
- `DELETE /api/v1/movies/<id>/`
  - **Descrição**: Deleta um filme.
  - **Permissão**: Apenas Admin.

### Avaliações (Reviews)

- `GET /api/v1/movies/<movie_id>/reviews/`
  - **Descrição**: Lista todas as avaliações de um filme específico.
  - **Permissão**: Aberto.
- `POST /api/v1/movies/<movie_id>/reviews/`
  - **Descrição**: Adiciona uma nova avaliação a um filme.
  - **Permissão**: Requer autenticação.
- `GET /api/v1/movies/<movie_id>/reviews/<review_id>/`
  - **Descrição**: Obtém uma avaliação específica.
  - **Permissão**: Aberto.
- `PUT /api/v1/movies/<movie_id>/reviews/<review_id>/`
  - **Descrição**: Atualiza uma avaliação.
  - **Permissão**: Apenas o autor da avaliação.
- `DELETE /api/v1/movies/<movie_id>/reviews/<review_id>/`
  - **Descrição**: Deleta uma avaliação.
  - **Permissão**: Apenas o autor da avaliação.

---

## 🖥️ Frontend

Esta API é consumida por uma aplicação frontend desenvolvida com Streamlit. Para ver a interface em ação e como ela interage com a API, visite o repositório do frontend:

- **[Streamlit Flix Frontend](https://github.com/alvarossantos/streamlit_flix_api)**
