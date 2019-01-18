#renderer
from colorama import *
from colorama.winterm import WinTerm

from .color import *
from .map import *

init()
win = WinTerm()

class Renderer:

    def __init__(self, screen):
        self.screen = screen

    def render_map(self, map):
        string = ""
        for y in range(len(map.walls)):
            for x in range(len(map.walls[y])):
                point = map.point(x, y)
                color = Color(color = point.color_glyph)
                if point.iswall:
                    string = string+str(color)+point.wall_glyph
                else:
                    string = string+str(color)+" "
            string = string+"\n"
        self.screen.reset()
        print(string)

    def render_player(self, map, player):
        background = map.point(player.x, player.y).color_glyph[2]
        forground = player.color[:2]
        color = forground+background
        color = Color(color=color)
        self.screen.cursor(player.x+1, player.y+1)
        if player.direction == "FORWARD":
            glyph = "^"
        elif player.direction == "LEFT":
            glyph = "<"
        elif player.direction == "RIGHT":
            glyph = ">"
        elif player.direction == "DOWN":
            glyph = "v"
        print(str(color)+glyph)
        self.screen.cursor(30, 30)
