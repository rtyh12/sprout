import numpy as np

from engine.components.sprite import Sprite
from engine.components.updateable import Updateable


class PlantScript(Updateable):
    sprite: Sprite

    def __init__(self) -> None:
        super().__init__()

    def start(self):
        sprite = self.get_components(Sprite)[0]
        self.sprite = sprite    # type: ignore (this can be sloppy)

    def update(self) -> None:
        new_arr = np.append(self.sprite.arr, np.array([['x']]), axis=1)
        self.sprite.arr = new_arr
