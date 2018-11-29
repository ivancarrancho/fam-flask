from fam.blud import FamObject
from fam.blud import NumberField
from fam.blud import StringField
from fam.fields import DateTimeField


class User(FamObject):
    use_rev = False
    additional_properties = False
    fields = {
        '_id': NumberField(),
        'name': StringField(),
        'phone': StringField(),
        'email': StringField(),
        'birth': DateTimeField(),
    }

    def get_user_data(self):
        return f'{self.name} - {self.phone} - {self.email} - {self.birth}'

    def pre_save_new_cb(self, obj):
        print(self)
        print('something after save')
        return True
