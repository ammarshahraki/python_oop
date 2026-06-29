from system.console import Console
from graphics.text import Text
from graphics.rectangle import Rectangle
from graphics.composite import Composite


class LineInput(Composite):
    def __init__(self, label, x, y, width):
        super().__init__()
        self._label = Text(label, x, y)
        self._box = Rectangle(x+self._label.width(), y-1, x+width, y+1)
        self._dummy = Text("", x+self._label.width()+1, y)

        self._components.append(self._label)
        self._components.append(self._box)
        self._components.append(self._dummy)
