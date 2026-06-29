import os
from ui.line_input import LineInput
from system.console import Console

if __name__ == "__main__":
    Console.clear()
    r1 = LineInput("Sample", 10, 10, 50)
    r1.paint()
    