from fam.blud import FamObject
from fam.blud import NumberField
from fam.blud import StringField
from fam.fields import DateTimeField


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
