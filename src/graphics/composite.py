from graphics.component import Component


class Composite(Component):
    def __init__(self):
        self._components: list[Component] = []

    def paint(self):
        for c in self._components:
            c.paint()
