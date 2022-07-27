import numpy as np
from .component_base import Component


class Sprite(Component):
    def __init__(self) -> None:
        self.arr = np.array([
            ['a', 'b', 'c'],
            ['a', 'x', 'c'],
            ['a', 'b', 'c'],
        ])

        self.center = (1, 1)

    @property
    def shape(self):
        return self.arr.shape

    def __repr__(self) -> str:
        return f"\nSprite object with center: {self.center}, content: \n{self.arr}"
