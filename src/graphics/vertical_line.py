from graphics.console import Console
from graphics.line import Line
class VLine(Line):

    def paint(self):
        for i in range(self._length):
            Console.gotoxy(self._x, self._y+i)
            print('│', end='')