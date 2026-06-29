from graphics.horizontal_line import HLine
from graphics.vertical_line import VLine

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self._top    = HLine(x1, y1, x2-x1)
        self._bottom = HLine(x1, y2, x2-x1)
        self._left   = VLine(x1, y1, y2-y1)
        self._right  = VLine(x2, y1, y2-y1)

    def paint(self):
        self._top.paint()
        self._bottom.paint()
        self._left.paint()
        self._right.paint()
        