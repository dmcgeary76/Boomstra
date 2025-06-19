# Boomstra

This project provides a simple authentication module with a basic user login feature.

## Usage

```
python -m boomstra.auth
```

You can add users programmatically:

```
from boomstra import auth
auth.add_user("username", "password")
```

Run tests with `pytest`.

## Django Project

A minimal Django project named **Boomstra** with an app called **Login** is included in the `Boomstra/` directory. After installing Django, you can run the development server with:

```bash
python Boomstra/manage.py runserver
```
