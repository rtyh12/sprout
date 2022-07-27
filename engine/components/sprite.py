import numpy as np
from .component_base import Component


class Sprite(Component):
    center: tuple[int, int]
    
    def __init__(self,
                 arr: np.ndarray = np.array([
                     ['0', '0', '0'],
                     ['0', 'x', '0'],
                     ['0', '0', '0'],
                 ])) -> None:
        self.arr = arr

        self.z_index = 0
        self.center = (1, 1)

    @property
    def shape(self):
        return self.arr.shape

    def __repr__(self) -> str:
        return f"Sprite component attached to {self.go_hash}"
