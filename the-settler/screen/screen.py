#screen
import colorama
from colorama.winterm import WinTerm
import os
import msvcrt
import time
import win32console

from keyboard import *
from renderer import *
from events import *

colorama.init()

win = WinTerm()

class Screen:

    def __init__(self):
        self.keyboard = Keyboard(self)
        self.renderer = Renderer(self)

        self.text = ""
        self.back = False

    def cursor_toggle(self, visible):
        console = win32console.CreateConsoleScreenBuffer()
        if visible:
            console.SetConsoleCursorInfo(1, True)
        else:
            console.SetConsoleCursorInfo(1, False)

    def render(self):
        pass

    def cursor(self, x=1, y=1):
        self.cursor_toggle(False)
        win.set_cursor_position((y,x))
        self.cursor_toggle(True)

    def clear(self):
        """
        THIS IS NOT GOOD TO USE, USE THIS SCARCELY
        """
        os.system('cls')

    def start(self):
        eventloop = EventLoop(self)
        eventloop.run()
