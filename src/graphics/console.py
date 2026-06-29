import sys

class Console:
    @classmethod
    def gotoxy(cls, x, y):
        print(f"{0x1b:c}[{y};{x}f", end='')

    @classmethod
    def clear(cls):
        print('\033c', end='')

    @classmethod
    def getch(cls):
        return sys.stdin.read(1)

