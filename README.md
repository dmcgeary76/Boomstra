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
