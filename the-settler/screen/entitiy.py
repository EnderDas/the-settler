#Entity
"""
No Gotdayum idea on how to handle entities... maybe have them in a seperate zipfile?
yea that sounds good...
its quite bothering how i talk to myself in the comments of my code...
:/
"""

class Entity:

    def __init__(self, name, **kwargs):
        self.name = name

class EntityFile(Entity):
    pass

class EntityFileHandler(EntityFile):
    pass
