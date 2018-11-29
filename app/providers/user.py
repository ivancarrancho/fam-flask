from injector import inject

from app.providers.couchdb import CouchDBProvider
from app.providers.fam import FamProvider

from app.models.user import User


class UserCouchDBProvider(object):

    @inject
    def __init__(self, database: CouchDBProvider):
        self.db = database.db

    def create_user(self):
        data = {
            '_id': 'julia30',  # Setting _id is optional
            'name': 'Julia',
            'age': 30,
            'pets': ['cat', 'dog', 'frog']
        }
        return self.db.create_document(data)


class UserFamProvider(object):

    @inject
    def __init__(self, database: FamProvider):
        self.db = database.db

    def create_user(
        self,
        name,
        phone,
        email,
        birth
    ):
        new_user = User(
            name=name,
            phone=phone,
            email=email,
            birth=birth
        )
        return self.db.put(new_user)
