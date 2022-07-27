class Transform:
    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pos

    def __repr__(self) -> str:
        return str(self.pos)

    def __str__(self) -> str:
        return self.__repr__()