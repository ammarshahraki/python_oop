from graphics.screen import Screen
from graphics.line import Line


class HLine(Line):
    def paint(self):
        Screen.gotoxy(self._x, self._y)
        for i in range(self._length):
            print('-', end='')
