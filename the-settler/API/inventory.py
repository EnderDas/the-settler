#inventory


from .frame import Frame as _Frame
from .weapon import Weapon as _Weapon
from .armor import Armor as _Armor
from .item import Item as _Item

class Inventory:

    def __init__(self, **kwargs):
        self.weapons = [_Weapon(wep) for wep in kwargs.get("weapons", [])]
        self.armors = [_Armor(arm) for arm in kwargs.get("armors", [])]
        self.items = [_Item(it) for it in kwargs.get("items", [])]

    @property
    def frame(self):
        return _Frame(self).dict
