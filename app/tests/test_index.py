import os
import pytest
import sqlite3
import tempfile
import click


from flask import current_app, g
from flask import Flask
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def init_db():
    db = get_db()

    with current_app.open_resource('data.sql') as f:
        db.executescript(f.read().decode('utf8'))


@pytest.fixture
def client():
    app = Flask(__name__)
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_index(client):
    response = client.get('/')
    print(client.get('/'))
    print(response.data)

    assert b"Crear usuario" in response.data
    assert b"Editar usuario" in response.data
