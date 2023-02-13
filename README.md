# Project Template by Luxu

## Como rodar o template?
* Crie um virtualenv com Python.
```
- Windows
python -m venv .venv
--------------------
- Linux
python3 -m venv .venv
```
* Ative o virtualenv.
```
Windows
.venv/Scripts/activate
--------------------
Linux
source .venv/bin/activate
```
* Instale o django
```
python.exe -m pip install --upgrade pip
pip install django

django-admin startproject --template https://github.com/luxu/template_default_django/archive/master.zip my_site
cd my_site
```
* Instale as dependências.
``
pip install -r requirements.txt
``
* Criar o *.env*
``python contrib/env_gen.py``
* Fazer as alterações necessárias
* Rode as migrações.
```
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
python manage.py runserver
```

Para o test com Pytest
* Instale as dependências.
``
pip install -r requirements-dev.txt
``
Na pasta **core** tem uma pasta **tests** onde devem ficar os tests