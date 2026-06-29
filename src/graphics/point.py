class Point():
    def __init__(self, char='.', x=0, y=0):
        self._x = x
        self._y = y
        self._char = char

    def paint(self):
        print(f"{0x1b:c}[{self._x};{self._y}f", end='')