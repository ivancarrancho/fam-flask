from flaskr import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    return app

# import os
# import tempfile

# import pytest
# from flaskr import create_app
# from flaskr.db import get_db, init_db
# from urllib.request import urlopen

# with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
#     _data_sql = f.read().decode('utf8')
# # file = 'http://127.0.0.1:5984/sensitive'
# # f = urlopen(file)
# # _data_sql = f.read().decode('utf8')
# print(_data_sql)
# print('_data_sql+++*************************')


# @pytest.fixture
# def app():
#     db_fd, db_path = tempfile.mkstemp()

#     app = create_app({
#         'TESTING': True,
#         'DATABASE': db_path,
#     })

#     with app.app_context():
#         init_db()
#         get_db().executescript(_data_sql)

#     yield app

#     os.close(db_fd)
#     os.unlink(db_path)


# @pytest.fixture
# def client(app):
#     return app.test_client()


# @pytest.fixture
# def runner(app):
#     return app.test_cli_runner()
