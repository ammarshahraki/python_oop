from system.console import Console
from graphics.component import Component

class Text():
    def __init__(self, content, x, y):
        self._x = x
        self._y = y
        self._content = content

    def paint(self):
        Console.gotoxy(self._x, self._y)
        print(self._content, end='')

    def width(self):
        return len(self._content)