#__init__

__version__ = "0.1.0a"

from API.__init__ import *
from API.Screen import *

"""
TODO

    1) Make a markdown "todo" file...
    2) Get rid of start.py and incorporate it into one file, use subproccess
       and commandline flags to start up the __init__ file maximized...
       (would be so much easier if i just used a different commandline interface).


    this was so long ago its crazy how much i made and yet still didn't finish it... i promise ill revive this project
       

"""
path = __file__.replace("__init__.py", "")
s = Screen()
p = MoveablePlayer()
m = Map(path+"testing")
s.render(m, p)
