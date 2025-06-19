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


## AddFamily Django App

The `addfamily` app provides a simple view that allows an authenticated user who
has the `is_parent` or `is_guardian` attribute to add children to a family
group. The form collects the child's name, preferred username and password and
creates a new user account for the child.

To include the app in a Django project, add `boomstra.addfamily` to
`INSTALLED_APPS` and include its URLs:

```python
# urls.py
path('family/', include('boomstra.addfamily.urls')),
```

The template `addfamily/add_child.html` extends `base_generic.html` and renders
the form.
=======
## Django Project

A minimal Django project named **Boomstra** with an app called **Login** is included in the `Boomstra/` directory. After installing Django, change into that directory and run the development server:

```bash
cd Boomstra
python manage.py runserver
```
