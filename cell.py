"""
Cell Class
attributes: color, x and y coords
"""


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.color = (0, 0, 0)

    def __repr__(self):
        return f'{self.__class__.__name__}(row={self.x}, column={self.y}, color={self.color})'

    def __str__(self):
        return f'Cell Row={self.x},Cell Column={self.y},Cell color={self.color}'

    def get_pos(self):
        return self.x, self.y

    def get_color(self):
        return self.color

    def set_color(self, color: str):
        self.color = color

    def set_pos(self, x: int, y: int):
        self.x = x
        self.y = y

    def neighbours(self):
        x, y = self.get_pos()
        return [(x + a[0], y + a[1]) for a in
                     [(-1, 0), (1, 0), (0, -1), (0, 1)]
                     if ((0 <= x + a[0] < 4) and (0 <= y + a[1] < 4))]
