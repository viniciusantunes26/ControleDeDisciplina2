# Controle De Disciplina

API Controle de Disciplina

Este projeto é uma API de gerenciamento de disciplinas onde Alunos terão certas tarefas.

# Visão Geral

Esta API fornece o gerenciamento de tarefas de cada aluno em determinadas disciplinas. Ela oferece criar, editar listar, deletar, listar detalhes de alunos, disciplinas e tarefas.

    Python 3.x
    Django 4.2.4
    Django Rest Framework 3.x

Configuração do Ambiente

Siga as etapas abaixo para configurar o ambiente de desenvolvimento:

    Clone o repositório:

*********

    No terminal, ative o Ambiente Virtual         python -m venv .env ./.venv/Scripts/activate

    Instale o requirements.txt                    pip install -r requirements.txt

    Crie um projeto                               django-admin startproject core .

    Crie um App para o desenvolvimento            python manage.py startapp nome/app


# COMANDO IMPORTANTES:

Para startar o projeto                                                                                                    git manage.py runserver
Descreve as alterações que devem ser feitas no banco de dados sempre que você cria, altera ou remove um modelo            git manage.py makemigrations 
É usado para aplicar ou desfazer migrações de banco de dados.                                                             git manage.py migrate 
