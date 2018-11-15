#color
from colorama import *

init()

class Color:

    codes = {
        "FOR_COLORS": {
            '0': Fore.BLACK,
            '1': Fore.RED,
            '2': Fore.GREEN,
            '3': Fore.YELLOW,
            '4': Fore.BLUE,
            '5': Fore.MAGENTA,
            '6': Fore.CYAN,
            '7': Fore.WHITE,
            '8': Style.BRIGHT+Fore.BLACK,
            '9': Style.BRIGHT+Fore.RED,
            'a': Style.BRIGHT+Fore.GREEN,
            'b': Style.BRIGHT+Fore.YELLOW,
            'c': Style.BRIGHT+Fore.BLUE,
            'd': Style.BRIGHT+Fore.MAGENTA,
            'e': Style.BRIGHT+Fore.CYAN,
            'f': Style.BRIGHT+Fore.WHITE
        },
        "BAC_COLORS":{
            '0': Back.BLACK,
            '1': Back.RED,
            '2': Back.GREEN,
            '3': Back.YELLOW,
            '4': Back.BLUE,
            '5': Back.MAGENTA,
            '6': Back.CYAN,
            '7': Back.WHITE,
            '8': Style.BRIGHT+Back.BLACK,
            '9': Style.BRIGHT+Back.RED,
            'a': Style.BRIGHT+Back.GREEN,
            'b': Style.BRIGHT+Back.YELLOW,
            'c': Style.BRIGHT+Back.BLUE,
            'd': Style.BRIGHT+Back.MAGENTA,
            'e': Style.BRIGHT+Back.CYAN,
            'f': Style.BRIGHT+Back.WHITE
        },
        "BRIGHTNESS": {
            '1': Style.NORMAL,
            '2': Style.BRIGHT,
            '3': Style.DIM
        }
    }

    def __init__(self, color = None, **kwargs):
        if color is None:
            self.foreground = kwargs.get('fore', 7)
            self.background = kwargs.get('back', 0)
            self.shade = kwargs.get('shade', 1)
            self.code = int('0x'+str(
                self.shade
                )+str(
                self.foreground
                )+str(
                self.background
                ), base=16)
        else:
            if isinstance(color, int):
                self.code = color
            else:
                self.code = int(color, base=16)

        #split up the parts of the code if given already

    def decode(self):
        """
          1  2  3
          |  |  |> Background
          |  |> Foreground
          |> Shade (Brightness)
        """

        hex_code = hex(self.code)[2:]
        brightness = self.codes['BRIGHTNESS'][hex_code[0]]
        foreground = self.codes['FOR_COLORS'][hex_code[1]]
        background = self.codes['BAC_COLORS'][hex_code[2]]

        codes = {
            "shade": brightness,
            "fore": foreground,
            "back": background
        }

        return codes
