#screen
import colorama
from colorama.winterm import WinTerm
import os
import msvcrt
import time
import win32console

from .color import *
from .renderer import *

colorama.init()

win = WinTerm()

class Screen:

    def __init__(self):
        self.text = ""
        self.back = False
        self.renderer = Renderer(self)

    def cursor_toggle(self, visible):
        console = win32console.CreateConsoleScreenBuffer()
        if visible:
            console.SetConsoleCursorInfo(1, True)
        else:
            console.SetConsoleCursorInfo(1, False)

    def render(self, map, player):
        self.renderer.render_map(map)
        self.renderer.render_player(map, player)

    def cursor(self, x=1, y=1):
        self.cursor_toggle(False)
        win.set_cursor_position((y,x))
        self.cursor_toggle(True)

    def reset(self):
        self.cursor()
