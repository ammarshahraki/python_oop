import os
from graphics.rectangle import Rectangle
from graphics.console import Console

if __name__ == "__main__":
    Console.clear()
    r1 = Rectangle(10, 10, 30, 20)
    r2 = Rectangle(5, 5, 40, 15)
    r1.paint()
    r2.paint()
    a = Console.getch()
    