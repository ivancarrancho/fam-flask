import os
from flask import Flask
from flask import render_template

from flask_injector import FlaskInjector

from app.providers.fam import FamProvider
from app.providers.couchdb import CouchDBProvider
from app.providers.user import UserCouchDBProvider
from app.providers.user import UserFamProvider
from app.providers.event import EventProvider

from app.endpoints.views import configure_views


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
        return 'hello'

    @app.route('/')
    def visit_home(name=None):
        return render_template('/index.html', name=name)

    configure_views(app)

    def configure(binder):
        binder.bind(FamProvider)
        binder.bind(CouchDBProvider)
        binder.bind(UserCouchDBProvider)
        binder.bind(UserFamProvider)
        binder.bind(EventProvider)

    FlaskInjector(app=app, modules=[configure])

    return app
