from graphics.console import Console
from graphics.line import Line


class HLine(Line):
    def paint(self):
        Console.gotoxy(self._x, self._y)
        for i in range(self._length):
            print('─', end='')
