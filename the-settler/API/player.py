#player


from .frame import Frame as _Frame
from .inventory import Inventory as _Inventory
from .weapon import Weapon as _Weapon
from .armor import Armor as _Armor

class Player:

    def __init__(self, **kwargs):
        """
        name
        level
        money
        inventory
        weapon
        armor
        """
        self.name = kwargs.get("name", None)
        self.level = kwargs.get("level", 1)
        self.money = kwargs.get("money", 0)
        try:
            inv = _Inventory(kwargs.get("inventory"))
        except:
            inv = _Inventory()
        try:
            wep = _Weapon(kwargs.get("weapon"))
        except:
            wep = _Weapon()
        try:
            arm = _Armor(kwargs.get("armor"))
        except:
            arm = _Armor()
        self.inventory = inv
        self.armor = arm
        self.weapon = wep

    @property
    def attack(self):
        attack = self.level
        attack *= ((self.weapon.impact/100)+1)
        attack *= self.weapon.power or 1
        return attack

    @property
    def defense(self):
        defense = self.level
        defense *= ((self.armor.protection/100)+1)
        defense *= self.armor.power or 1
        return attack

    @property
    def frame(self):
        return _Frame(self).dict
