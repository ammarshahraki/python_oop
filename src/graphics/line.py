from graphics.console import Console
from graphics.component import Component

class Line(Component):
    def __init__(self, x, y, length):
        self._x = x
        self._y = y
        self._length = length
