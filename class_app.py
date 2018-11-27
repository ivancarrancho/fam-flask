from fam.blud import FamObject
from fam.blud import NumberField
from fam.blud import StringField
from fam.fields import DateTimeField

# https://github.com/paulharter/fam/issues/1
# from fam.string_formats import DateTimeField
# from fam.string_formats import EmailField


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


class Call(FamObject):
    use_rev = False
    additional_properties = False
    fields = {
        '_id': NumberField(),
        'req': StringField(),
        'date': DateTimeField(),
    }

    def get_calls_data(self):
        return f'{self.req} - {self.date}'
