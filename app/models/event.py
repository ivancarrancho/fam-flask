from fam.blud import FamObject
from fam.blud import NumberField
from fam.blud import StringField


class Event(FamObject):
    use_rev = False
    additional_properties = False
    fields = {
        '_id': NumberField(),
        'state': StringField(),
    }

    def get_calls_data(self):
        return f'{self.req} - {self.date}'