from .component_base import Component
from .transform import Transform


class Updateable(Component):
    def __init__(self, transform: Transform) -> None:
        super().__init__()
        self.transform = transform

    def update(self):
        print('updating')
