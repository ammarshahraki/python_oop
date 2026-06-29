from graphics.composite import Composite
from graphics.horizontal_line import HLine
from graphics.vertical_line import VLine
from graphics.point import Point

class Rectangle(Composite):
    def __init__(self, x1, y1, x2, y2):
        self._components =[
            HLine(x1, y1, x2-x1),
            HLine(x1, y2, x2-x1),
            VLine(x1, y1, y2-y1),
            VLine(x2, y1, y2-y1),
            Point('┌', x1, y1),
            Point('└', x1, y2),
            Point('┐', x2, y1),
            Point('┘', x2, y2),
        ]
