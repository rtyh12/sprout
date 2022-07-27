from typing import Type
import random
import string

from .components.component_base import Component
from .components.transform import Transform
from .components.updateable import Updateable
from .components.sprite import Sprite

from .systems.render import render


class Player:
    def __init__(self) -> None:
        self.inventory = {}
        self.id = 0


class Game:
    def __init__(self) -> None:
        self.players = []
        self.game_objects = {}
        go_hash = self.add_game_object(Transform((5, 5)))
        self.add_component(go_hash, Sprite())

    def add_game_object(self, transform: Transform) -> str:
        # generate random hash
        hash = ''.join(random.choices(
            string.ascii_letters + string.digits, k=32))
        self.game_objects[hash] = [transform]
        return hash

    def add_component(self, hash: str, component: Component) -> None:
        self.game_objects[hash].append(component)

    def get_component(self, hash: str, type_: Type[Component]) -> Component:
        pass

    def transform_and_components_of_type(self, type_: Type[Component]) \
            -> dict[Transform, list[Component]]:
        return {
            # find first Transform
            next(obj for obj in components if isinstance(obj, Transform)):
            # find all components of requested type
            [c for c in components if isinstance(c, type_)]
            for components in self.game_objects.values()
        }

    def components_of_type(self, type_: Type[Component]):
        return [
            c for c in
            [component for component in self.game_objects.values()]
        ]

    def update(self) -> None:
        updateables = self.transform_and_components_of_type(Updateable)
        for transform, us in updateables.items():
            for updateable in us:
                updateable.update(transform)

    def render(self) -> str:
        renderables = self.transform_and_components_of_type(Sprite)
        self.graphics = render(renderables)
        return self.graphics

    def player_join(self) -> None:
        player = Player()
        player.id = 0
        player.inventory = {'seed': 1}
        self.players.append(player)
