import numpy as np
import numpy.typing as npt
from .component_base import Component


class Sprite(Component):
    center: tuple[int, int]
    arr: npt.NDArray[np.string_]
    
    def __init__(self,
                 arr: np.ndarray = np.array([
                     ['0', '0', '0'],
                     ['0', 'x', '0'],
                     ['0', '0', '0'],
                 ])) -> None:
        if arr.dtype != np.string_:
            arr = arr.astype(np.string_)

        self.arr = arr
        self.z_index = 0
        self.center = (1, 1)

    @property
    def shape(self):
        return self.arr.shape

    def __repr__(self) -> str:
        return f"Sprite component attached to {self.go_hash}"
