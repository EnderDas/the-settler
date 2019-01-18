#keyboard
import msvcrt
import time

class Keyboard:

    def __init__(self, console):
        self.console = console
        self.c_x = 1
        self.c_y = 1

    def get_key(self):
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
                return ord(second)
        else:
            return key

    def key_press(self):
        pass
