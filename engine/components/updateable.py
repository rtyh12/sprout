from .component_base import Component


class Updateable(Component):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        if type(self) == Updateable:
            print(f'start() called on generic Updateable of {self.go_hash}')

    def update(self):
        if self.go_hash is None:
            raise ValueError("go_hash is None (is this component attached to a game object?)")
        if type(self) == Updateable:
            print(f'update() called on generic Updateable of {self.go_hash}')
