#armor

"""
Types
Leather
Treated Leather
Chainmail
Iron
Steel
"""

from .frame import Frame as _Frame

class Mod:

    def __init__(self, **kwargs):
        """
        name
        hidden
        buffs
        """
        self.name = kwargs.get("name", "Mod")
        self.hidden = kwargs.get("hidden", False)
        self.buffs = kwargs.get("buffs", {})

    @property
    def frame(self):
        return _Frame(self).dict

_leather_base = Mod(name="leatherbase", hidden=True, buffs={
    "protection": 30,
    "resistance": 30
})

_treatedleather_base = Mod(name="treatedleatherbase", hidden=True, buffs={
    "protection": 30,
    "resistance": 40
})

_chainmail_base = Mod(name="chainmailbase", hidden=True, buffs={
    "protection": 40,
    "resistance": 40
})

_iron_base = Mod(name="ironbase", hidden=True, buffs={
    "protection": 50,
    "resistance": 50
})

_steel_base = Mod(name="ironbase", hidden=True, buffs={
    "protection": 60,
    "resistance": 60
})

_TYPES = {
    "leather": _leather_base,
    "treatedleather": _treatedleather_base,
    "chainmail": _chainmail_base,
    "iron": _iron_base,
    "steel": _steel_base
}

class Armor:

    def __init__(self, **kwargs):
        """
        name
        type
        mods
        """
        self.name = kwargs.get("name", "Armor")
        self.type = kwargs.get("type", "leather")
        self.mods = [Mod(dict(mod)) for mod in kwargs.get("mods", [])]
        self.stats = {
            "protection": 0,
            "resistance": 0,
            "power": 0
            }
        if _TYPES[self.type] in self.mods:
            pass
        else:
            self.mods.append(_TYPES[self.type])

        for mod in self.mods:
            for buff in mod.buffs:
                if buff in self.stats:
                    self.stats[buff] += mod.buffs[buff]

    @property
    def protection(self):
        return self.stats.protection

    @property
    def resistance(self):
        return self.stats.resistance

    @property
    def power(self):
        return self.stats.power

    @property
    def frame(self):
        return _Frame(self).dict
