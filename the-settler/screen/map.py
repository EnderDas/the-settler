#Map
import zipfile

class Point:

    def __init__(self, **kwargs):
        self.wallCode = kwargs.get("wallCode", 0)
        self.itemCode = kwargs.get("itemCode", 0)
        #self.entityCode = kwargs.get("entityCode", 0)
        self.colorCode = kwargs.get("colorCode", 0)
        self.parentMap = kwargs.get("parentMap", None)
        self.isWall = kwargs.get("isWall", False)
        self.hasItem = kwargs.get("hasItem", False)
        #self.hasEntity = kwargs.get("hasEntity", False)

class MapHandler:

    def __init__(self, walls, items, colors, color_matrix):
        self.walls = [[i for i in k] for k in walls.splitlines()]
        self.items = [[i for i in k] for k in items.splitlines()]
        #self.entities = [[i for i in k] for k in entities.splitlines()]
        self.colors = [[i for i in k] for k in colors.splitlines()]
        self.color_matrix = color_matrix
        self.x = len(max(self.walls, key=len))
        self.y = len(self.walls)

    def point_data(self, x, y):
        _wallCode = self.walls[y][x]
        _itemCode = self.items[y][x]
        #_entityCode = self.entities[y][x]
        _colorCode = self.color_matrix[self.colors[y][x]]
        _parentMap = self
        _isWall = True if int(_wallCode) == 1 else False
        _hasItem = True if int(_itemCode) > 0 else False
        #_hasEntity = True if _entityCode > 0 else False

        args  = {
            "wallCode": _wallCode,
            "itemCode": _itemCode,
            #"entityCode": _entityCode,
            "colorCode": _colorCode,
            "parentMap": _parentMap,
            "isWall": _isWall,
            "hasItem": _hasItem,
            #{}"hasEntity": _hasEntity
        }

        point = Point(**args)

        return point

class MapFile(MapHandler):

    def __init__(self, filename):
        self.filename = filename+".zip"

        with zipfile.ZipFile(self.filename) as file:

            with file.open(filename+"/walls", 'r') as fp:
                _walls = fp.read().decode()

            with file.open(filename+"/items", 'r') as fp:
                _items = fp.read().decode()

            #_entities = self.filename+"/entities"

            with file.open(filename+"/colors", 'r') as fp:
                _colors = fp.read().decode()

            with file.open(filename+"/color_matrix", 'r') as fp:
                cmx = fp.read()
                cmx = cmx.decode().splitlines()
                _color_matrix = {}
                for i in cmx:
                    cmx2 = i.split(" ")
                    _color_matrix[cmx2[0]] = cmx2[1].strip("\r\n")

        super().__init__(
            _walls, _items,
            #_entities,
            _colors,
            _color_matrix
        )


m = MapFile("testing")
p = m.point_data(0,0)
