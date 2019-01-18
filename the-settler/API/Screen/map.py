#map
class Point:

    def __init__(self, **kwargs):
        self.iswall = kwargs.get("iswall", None)
        self.wall_glyph = kwargs.get("wall_glyph", None)
        self.color_glyph = kwargs.get("color_glyph", None)
        self.item = kwargs.get("item", None)

class Map:

    def __init__(self, filename):
        self.filename = filename

        with open(filename+".tmmf", 'r') as fp:
            file = fp.read()

        self.raw_file = file
        self.lines = self.raw_file.splitlines()
        self.split_lines = [i.split() for i in self.lines]

        self.index_lines = {
            "WALL": [],
            "WALL_MATRIX": [],
            "COLOR": [],
            "COLOR_MATRIX": [],
            "ITEMS": [],
            "INIT": []
        }

        self.vars = {
            "BASE": {
                "WALL": None,
                "WALL_MATRIX": None,
                "COLOR": None,
                "COLOR_MATRIX": None,
                "ITEMS": None
            },
            "INIT": {
                "NAME": None,
                "FORMATTER": None
            },
            "DECLARES": {}
        }

        self.decode_file()

    def point(self, x, y):
        if int(self.walls[y][x]) > 0:
            _iswall = True
            _wall_glyph = self.wall_matrix[self.walls[y][x]]
        else:
            _iswall = False
            _wall_glyph = " "
        _color_glyph = self.color_matrix[self.colors[y][x]]
        _item = self.items[y][x]
        p = Point(
            iswall = _iswall,
            wall_glyph = _wall_glyph,
            color_glyph = _color_glyph,
            item = _item
        )
        return p

    @property
    def walls(self):
        wall_stuff = [[k for k in i] for i in self.vars["BASE"]["WALL"]]
        return wall_stuff

    @property
    def wall_matrix(self):
        wall_stuff = {i.split()[0] : i.split()[1] for i in self.vars["BASE"]["WALL_MATRIX"]}
        return wall_stuff

    @property
    def colors(self):
        color_stuff = [[k for k in i] for i in self.vars["BASE"]["COLOR"]]
        return color_stuff

    @property
    def color_matrix(self):
        color_stuff = {i.split()[0] : i.split()[1] for i in self.vars["BASE"]["COLOR_MATRIX"]}
        return color_stuff

    @property
    def items(self):
        items_stuff = [[k for k in i] for i in self.vars["BASE"]["ITEMS"]]
        return items_stuff


    def decode_file(self):

        #find all declares
        self.find_declares()

        #find all item index
        self.find_indexs()

        #load all vars
        self.load_vars()

    def load_vars(self):
        #load base vars
        self.load_base_vars()
        self.load_init_vars()
        self.load_declared_vars()

    def load_declared_vars(self):
        lists = self.vars["DECLARES"].keys()
        for items in lists:
            for things in range(self.index_lines[items][0]+1, self.index_lines[items][1]):
                item = self.lines[things]
                split_item = item.split()
                del split_item[1]
                self.vars["DECLARES"][items][split_item[0]] = split_item[1]

    def load_init_vars(self):
        init = [
            "NAME", "FORMATTER"
        ]
        for things in range(self.index_lines["INIT"][0]+1, self.index_lines["INIT"][1]):
            item = self.lines[things]
            split_item = item.split()
            del split_item[1]
            self.vars["INIT"][split_item[0]] = split_item[1]

    def load_base_vars(self):
        base = [
            "WALL", "WALL_MATRIX", "COLOR", "COLOR_MATRIX", "ITEMS"
        ]
        for thing in base:
            lines = [
                self.lines[line] for line in range(self.index_lines[thing][0]+1, self.index_lines[thing][1])
            ]
            self.vars["BASE"][thing] = lines

    def find_indexs(self):
        for lines in range(len(self.split_lines)):
            if "START" in self.split_lines[lines]:
                name2 = self.split_lines[lines][2]
                self.index_lines[name2].append(lines)
                for lines2 in range(lines, len(self.split_lines)):
                    if "END" in self.split_lines[lines2]:
                        self.index_lines[name2].append(lines2)
                        break

    def find_declares(self):
        for lines in self.split_lines:
            if "DECLARE" in lines:
                name = lines[2]
                self.index_lines[name] = []
                self.vars["DECLARES"][name] = {}
                break

if __name__ == "__main__":
    try:
        map = Map("testing")
        print("Maps working correctly!")
    except:
        print(":/")
