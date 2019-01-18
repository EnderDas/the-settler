#__init__

__version__ = "0.1.0a"

from API.__init__ import *
from API.Screen import *

"""
TODO

    1) Make a markdown "todo" file...
    2) Get rid of start.py and incorportate it into one file, use subproccess
       and commandline flags to start up the __init__ file maximized...
       (would be so much easier if i just used a different commandline interface).

       

"""

s = Screen()
p = MoveablePlayer()
m = Map("testing")
s.render(m, p)
