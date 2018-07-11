#item

from .frame import Frame as _Frame

class Item:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.buff = kwargs.get("buff", [])
        self.cost = kwargs.get("cost", 0)

    @property
    def frame(self):
        return _Frame(self).dict
