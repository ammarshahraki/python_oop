from graphics.console import Console
from graphics.component import Component

class Point():
    def __init__(self, char, x, y):
        self._x = x
        self._y = y
        self._char = char

    def paint(self):
        Console.gotoxy(self._x, self._y)
        print(self._char, end='')