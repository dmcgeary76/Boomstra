import os
import tempfile

from boomstra import auth


def test_add_and_authenticate_user(tmp_path):
    users_file = tmp_path / "users.json"
    # patch USERS_FILE
    old_file = auth.USERS_FILE
    auth.USERS_FILE = str(users_file)
    try:
        auth.add_user("alice", "secret")
        assert auth.authenticate("alice", "secret")
        assert not auth.authenticate("alice", "wrong")
        assert not auth.authenticate("bob", "secret")
    finally:
        auth.USERS_FILE = old_file
