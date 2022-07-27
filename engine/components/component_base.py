from __future__ import annotations

from typing import Union, Type


class Component:
    go_hash: Union[str, None] = None
    # TODO why do forward annotations not seem to work properly??
    game: Union[Game, None]     # type: ignore # noqa

    def get_components(self, type_: Type[Component]) -> list[Component]:
        assert self.go_hash is not None
        assert self.game is not None
        return self.game.get_components(self.go_hash, type_)
