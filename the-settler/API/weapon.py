#weapons

"""
Weapon types

Handgun
Rifle
Machine Gun
Shotgun
Cross Bow
Bolt Rifle

Weapon Stat Basis

100/100

Impact
Accuracy
Speed
Power
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

_handgun_base = Mod(name="handgunbase", hidden=True, buffs={
    "impact": 70,
    "accuracy": 50,
    "speed": 40
})

_rifle_base = Mod(name="riflebase", hidden=True, buffs={
    "impact": 50,
    "accuracy": 50,
    "speed": 50
})

_machinegun_base = Mod(name="machinegunbase", hidden=True, buffs={
    "impact": 40,
    "accuracy": 40,
    "speed": 70
})

_shotgun_base = Mod(name="shotgunbase", hidden=True, buffs={
    "impact": 30,
    "accuracy": 40,
    "speed": 50
})

_crossbow_base = Mod(name="crossbowbase", hidden=True, buffs={
    "impact": 40,
    "accuracy": 70,
    "speed": 40
})

_boltrifle_base = Mod(name="boltriflebase", hidden=True, buffs={
    "impact": 50,
    "accuracy": 80,
    "speed": 50
})

_TYPES = {
    "handgun": _handgun_base,
    "rifle": _rifle_base,
    "machinegun": _machinegun_base,
    "shotgun": _shotgun_base,
    "crossbow": _crossbow_base,
    "boltrifle": _boltrifle_base,
}

class Weapon:

    def __init__(self, **kwargs):
        """
        name
        type
        mods
        """
        self.name = kwargs.get("name", "Weapon")
        self.type = kwargs.get("type", "handgun")
        self.mods = [Mod(dict(mod)) for mod in kwargs.get("mods", [])]
        self.stats = {
                    "impact": 0,
                    "accuracy": 0,
                    "speed": 0,
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
    def impact(self):
        return self.stats.impact

    @property
    def accuracy(self):
        return self.stats.accuracy

    @property
    def speed(self):
        return self.stats.speed

    @property
    def power(self):
        return self.stats.power

    @property
    def frame(self):
        return _Frame(self).dict
