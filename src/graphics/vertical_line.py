from graphics.screen import Screen
from graphics.line import Line
class VLine(Line):

    def paint(self):
        for i in range(self._length):
            Screen.gotoxy(self._x, self._y+i)
            print('|', end='')