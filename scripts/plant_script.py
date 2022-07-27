from engine.components.sprite import Sprite
from engine.components.updateable import Updateable


class PlantScript(Updateable):
    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        print('update plant')
        print(self.get_components(Sprite))
