from components.sprite import Sprite
from components.transform import Transform

from systems.render import render


class Player:
    def __init__(self) -> None:
        self.inventory = {}
        self.id = 0


class Game:
    def __init__(self) -> None:
        self.players = []
        self.game_objects = {
            Transform((0, 0)): [Sprite()]
        }

    def update(self):
        pass

    def render(self):
        for transform, components in self.game_objects.items():
            print(transform, components)

        renderables = {
            transform: [c for c in components if type(c) == Sprite]
            for transform, components in self.game_objects.items()
        }
        self.graphics = render(renderables)
        print(self.graphics)

    def player_join(self):
        player = Player()
        player.id = 0
        player.inventory = {'seed': 1}
        self.players.append(player)
