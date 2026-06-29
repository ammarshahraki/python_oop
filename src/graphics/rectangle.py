from graphics.composite import Composite
from graphics.horizontal_line import HLine
from graphics.vertical_line import VLine
from graphics.text import Text

class Rectangle(Composite):
    def __init__(self, x1, y1, x2, y2):
        self._components =[
            HLine(x1, y1, x2-x1),
            HLine(x1, y2, x2-x1),
            VLine(x1, y1, y2-y1),
            VLine(x2, y1, y2-y1),
            Text('┌', x1, y1),
            Text('└', x1, y2),
            Text('┐', x2, y1),
            Text('┘', x2, y2),
        ]
