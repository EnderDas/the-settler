#__init__
from ctypes import *
import os
import msvcrt
import colorful
#os.system('mode 80, 30')

STD_OUTPUT_HANDLE = -11

class _COORD(Structure):
    pass

_COORD._fields_ = [("X", c_short), ("Y", c_short)]

class Screen:

    def __init__(self, matrix, slot):
        self.width, self.height = os.get_terminal_size()
        self.cursor = [0, 0]
        self.playerx = 1
        self.playery = 1
        self.slot = slot
        self.matrix = matrix

    def find_player(self):
        for y in range(len(self.matrix)):
            for x in range(len(max(self.matrix, key=max))):
                if self.matrix[y][x] == self.slot:
                    self.playerx = x
                    self.playery = y

    def move(self, x, y):
        self.playerx = x
        self.playery = y

    def render(self, dirr):
        self.refresh()
        map = ''
        for y in self.matrix:
            _x = ''
            for x in y:
                if x == '1':
                    _x = _x+"+"
                elif x == '2':
                    _x = _x+'='
                elif x == '3':
                    _x = _x+'|'
                elif x == '0':
                    _x = _x+' '
                else:
                    _x = _x+x
            map = map+_x+'\n'
        print(map)
        self.move_cur([self.playerx, self.playery])
        direct = {
            "up": "^",
            "down": "v",
            "left": "<",
            "right": ">"
        }
        print(colorful.yellow(direct[dirr]))
        self.move_cur([0, len(self.matrix)])


    def refresh(self, pos=None):
        if pos == None:
            cursor = self.cursor
        else:
            cursor = pos
        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, _COORD(cursor[0], cursor[1]))

    def move_cur(self, cursor):
        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, _COORD(cursor[0], cursor[1]))

mat = """122222121221
300000303003
300000003003
300000303003
122222101201
300000000003
122222222221"""

def Matrix(string):
    matrix = [[i for i in k] for k in string.splitlines()]
    return matrix

matrix = Matrix(mat)

def get_key():
    key = msvcrt.getwch()
    if ord(key) == 224:
        second = msvcrt.getwch()
        if ord(second) == 72:
            return 'KEY_UP'
        elif ord(second) == 80:
            return 'KEY_DOWN'
        elif ord(second) == 75:
            return 'KEY_LEFT'
        elif ord(second) == 77:
            return 'KEY_RIGHT'
        else:
            return 'UNKNOWN'
    else:
        return key

s = Screen(matrix, '8')
s.find_player()

direct = {
    "up": "^",
    "down": "v",
    "left": "<",
    "right": ">"
}

DIR = "down"

while True:
    key = get_key()
    if key == 'KEY_UP':
        try:
            DIR = "up"
            if int(s.matrix[s.playery-1][s.playerx]) > 0:
                pass
            else:
                s.move(s.playerx, s.playery-1)
        except:
            pass
    elif key == 'KEY_DOWN':
        try:
            DIR = "down"
            if int(s.matrix[s.playery+1][s.playerx]) > 0:
                pass
            else:
                s.move(s.playerx, s.playery+1)
        except:
            pass
    elif key == 'KEY_LEFT':
        try:
            DIR = "left"
            if int(s.matrix[s.playery][s.playerx-1]) > 0:
                pass
            else:
                s.move(s.playerx-1, s.playery)
        except:
            pass
    elif key == 'KEY_RIGHT':
        try:
            DIR = "right"
            if int(s.matrix[s.playery][s.playerx+1]) > 0:
                pass
            else:
                s.move(s.playerx+1, s.playery)
        except:
            pass
    else:
        pass
    s.render(DIR)
    print("""
+-----------------+
|Use arrow keys to|
|   move around   |
+-----------------+
""")
