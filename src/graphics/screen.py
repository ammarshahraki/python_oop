class Screen:
    @classmethod
    def gotoxy(cls, x, y):
        print(f"{0x1b:c}[{y};{x}f", end='')

    @classmethod
    def clear(cls):
        print('\033c', end='')