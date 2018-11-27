import os
from flask import Flask
from flask import render_template
from flask import request

from fam.mapper import ClassMapper
from fam.database import CouchDBWrapper

from class_app import Call
from class_app import User


def create_app(test_config=None):
    app = Flask(__name__)
    # create and configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    mapper = ClassMapper([User, Call])
    db = CouchDBWrapper(
        mapper,
        'http://127.0.0.1:5984/',
        'sensitive'
    )

    @app.route('/')
    def visit_home(name=None):
        return render_template('/index.html', name=name)

    @app.route(
        '/user',
        methods=['POST']
    )
    def create_user():
        if request.method == 'POST':

            new_user = User(
                name=request.form['name'],
                phone=request.form['phone'],
                email=request.form['email'],
                birth=request.form['birth']
            )

            db.put(new_user)

            return 'se creó el usuario correctamente'
        return 'no recibo consultas por get'

    @app.route(
        '/editar',
        methods=['POST']
    )
    def edit_user():
        if request.method == 'POST':
            old_user = db.get(request.form['key'])
            old_user.name = request.form['new_name']
            db.put(old_user)

            return 'se re nombró usuario correctamente'
        return 'no recibo consultas por get'

    @app.route(
        '/delete',
        methods=['POST']
    )
    def delete_user():
        if request.method == 'POST':
            old_user = db.get(request.form['key'])
            if old_user:
                db.delete(old_user)

                return 'se eliminó el usuario correctamente'
            return 'Usuario no existe'
        return 'no recibo consultas por get'

    return app
