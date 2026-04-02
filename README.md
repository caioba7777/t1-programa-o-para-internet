# 📦 TechStore Manager — Sistema Web com Flask

## 📌 Descrição do Projeto

O **TechStore Manager** é um sistema web desenvolvido com o framework Flask, com o objetivo de simular um ambiente de gestão comercial voltado para lojas de tecnologia.

O sistema foi desenvolvido como parte da atividade avaliativa (T1), aplicando conceitos fundamentais de desenvolvimento web, como organização de projeto, rotas, templates com herança (Jinja2), estilização com CSS e uso do framework Bootstrap.

Não há integração com banco de dados nesta versão. Os dados são simulados utilizando estruturas em Python, conforme os requisitos do trabalho.

---

## 🎯 Objetivos

* Desenvolver um sistema web funcional utilizando Flask
* Aplicar o conceito de rotas e navegação entre páginas
* Utilizar templates com herança (Jinja2)
* Criar interfaces com Bootstrap e CSS personalizado
* Simular operações de cadastro e listagem de dados
* Estruturar corretamente um projeto web

---

## ⚙️ Funcionalidades

O sistema possui as seguintes funcionalidades:

### 🔐 Autenticação

* Tela de login (simulada)
* Cadastro de novo usuário
* Logout com redirecionamento

### 👤 Gestão de Usuários

* Listagem de usuários
* Inserção de novos usuários
* Validação de campos obrigatórios

### 📦 Gestão de Produtos

* Listagem de produtos
* Inserção de novos produtos
* Controle de preço, estoque e categoria

### 🗂️ Gestão de Categorias

* Listagem de categorias
* Inserção de novas categorias
* Organização por setor e status

### 👨‍💻 Página da Equipe

* Apresentação dos desenvolvedores
* Informações como nome, e-mail e mini bio

---

## 🧱 Estrutura do Projeto

O projeto segue a estrutura padrão do Flask:

```
trabalho-ronan/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── base_publica.html
│   ├── index.html
│   ├── login.html
│   ├── cadastro.html
│   ├── sobre_equipe.html
│   │
│   ├── usuarios/
│   ├── produtos/
│   └── categorias/
│
└── static/
    ├── css/
    └── js/
```

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **Jinja2 (templates)**

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
cd NOME_DO_REPO
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o projeto

```bash
python app.py
```

### 5. Acessar no navegador

```
http://127.0.0.1:5000
```

---

## 📋 Observações

* O sistema não utiliza banco de dados, conforme especificado no trabalho
* Os dados são armazenados em listas Python (simulação)
* As operações de inserção não persistem após reiniciar a aplicação
* As ações de editar e excluir são apenas visuais nesta versão

---

## 👨‍🎓 Desenvolvedores

* **Caio Daniel Reis da Silva**


---

## 📚 Considerações Finais

Este projeto foi desenvolvido com o objetivo de consolidar os conhecimentos iniciais em desenvolvimento web com Flask, proporcionando experiência prática na criação de sistemas organizados, com navegação funcional e interface amigável.

---
