from flask.views import MethodView
from flask import request
from injector import inject

from app.providers.user import UserFamProvider


class UserAPI(MethodView):

    @inject
    def __init__(self, user_provider: UserFamProvider):
        self.user = user_provider

    def get(self):
        return 'hello'

    def post(self):
        self.user.create_user(
            request.form['name'],
            request.form['phone'],
            request.form['email'],
            request.form['birth']
        )
        return 'user created'
