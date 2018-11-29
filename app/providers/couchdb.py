from cloudant.client import CouchDB


class CouchDBProvider(object):

    def __init__(self):
        self.db_client = CouchDB(
          'admin',
          'SHFJ3QrCBNJAq8pc47LnhxBLsaAfzu',
          url='http://172.104.154.154:5985',
          connect=True
        )
        self.db = self.db_client['sensitive']
