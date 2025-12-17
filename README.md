# CRM Django - Sistema de Gestão de Clientes

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2%2B-green)

## 💻 Sobre o projeto

Este projeto é um sistema de **CRM (Customer Relationship Management)** simplificado, desenvolvido para praticar operações de CRUD e gerenciamento de banco de dados com Django. 

O sistema permite o cadastro, visualização, edição e exclusão de clientes, centralizando as informações em uma interface web intuitiva.

## ✨ Funcionalidades

* [x] Cadastro de novos clientes.
* [x] Listagem dinâmica de clientes cadastrados.
* [x] Edição de dados existentes.
* [x] Exclusão de registros do banco de dados.
* [x] Painel administrativo do Django configurado.

## 🛠 Tecnologias Utilizadas

* **Python**
* **Django** (Framework Web)
* **SQLite** (Banco de dados)
* **HTML/CSS** para as interfaces

## 📂 Estrutura do Repositório

Conforme a organização do projeto:
* **`clientes/`**: Módulo responsável pela lógica de negócio e interface do CRM.
* **`crm_django/`**: Configurações centrais do projeto (URLs, Settings, WSGI).
* **`manage.py`**: Script de interface para comandos do Django.

## 🚀 Como rodar o projeto

Siga os passos abaixo:

```bash
## 🚀 Como rodar o projeto

> **⚠️ Requisito de Banco de Dados:** Este projeto utiliza **MySQL**. Certifique-se de que o serviço do MySQL esteja ativo (via XAMPP ou MySQL Installer) e que você tenha criado o esquema (database) no **MySQL Workbench** antes de prosseguir.

```bash
# 1. Clone o repositório
$ git clone [https://github.com/ViniciusS4ntos/Crud-python-Django.git](https://github.com/ViniciusS4ntos/Crud-python-Django.git)

# 2. Entre na pasta do projeto
$ cd Crud-python-Django/crm_django

# 3. Crie e ative o ambiente virtual
$ python -m venv venv
# Windows: venv\Scripts\activate | Linux/Mac: source venv/bin/activate

# 4. Instale o Django e o conector MySQL
$ pip install django mysqlclient

# 5. Configure o banco no Workbench e ative o SQL

# 6. Rode as migrações
$ python manage.py migrate

# 7. Inicie o servidor
$ python manage.py runserver
