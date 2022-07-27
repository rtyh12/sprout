from __future__ import annotations
import numpy as np

X_AXIS_LABELS = (
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '!@#$%^&*()-=_+/.,:;{}[]<>?~αβγδεζηθικλμνξοπρστυφχψω'
)


def add_borders(arr: np.ndarray) -> np.ndarray:
    max_number_width = (len(str(arr.shape[0])), len(str(arr.shape[1])))

    x_axis_numbers = []
    for x in range(arr.shape[0]):
        s = X_AXIS_LABELS[x]
        s += '-'
        a = np.array(list(s), dtype=np.str_)
        x_axis_numbers.append(a)
    x_axis_numbers = np.stack(x_axis_numbers)

    y_axis_numbers = []
    for x in range(arr.shape[1]):
        s = str(x + 1).rjust(max_number_width[1]) + ": "
        a = np.array(list(s), dtype=np.str_)
        y_axis_numbers.append(a)
    y_axis_numbers = np.stack(y_axis_numbers)

    arr = np.concatenate([x_axis_numbers, arr], axis=1)

    y_axis_numbers = np.rot90(y_axis_numbers)[::-1]

    y_axis_numbers = np.pad(y_axis_numbers,
                            (
                                (0, 0),
                                (x_axis_numbers.shape[1], 0),   # type: ignore
                            ),
                            'constant',                         # type: ignore
                            constant_values=(' '))

    arr = np.concatenate([y_axis_numbers, arr], axis=0)

    return arr


def array_to_string(arr: np.ndarray) -> str:
    out = '```\n'

    for y in reversed(range(arr.shape[1])):
        for x in range(arr.shape[0]):
            out += arr[x, y]
        out += '\n'

    out += '```'

    return out


def render(renderables: dict[Transform, Sprite], size=(25, 20)) -> str:     # type: ignore # noqa
    out = np.zeros(size, np.str_)
    for x in range(size[0]):
        col = np.zeros(size[1], np.str_)
        col = '⋅'
        out[x, :] = col

    to_render = []
    for transform, sprites in renderables.items():
        for sprite in sprites:
            to_render.append((transform, sprite))

    to_render.sort(key=lambda t: t[1].z_index)

    for transform, sprite in to_render:
        # Calculate bounding box in world coords
        left = transform.pos[0] - sprite.center[0]
        bottom = transform.pos[1] - sprite.center[1]
        right = left + sprite.shape[0]
        top = bottom + sprite.shape[1]

        # Chop off parts of bbox outside of the viewport
        arr_to_render = sprite.arr.copy()

        if left < 0:
            arr_to_render = arr_to_render[-left:, :]
            left = 0
        if bottom < 0:
            arr_to_render = arr_to_render[:, -bottom:]
            bottom = 0
        if right >= size[0]:
            arr_to_render = arr_to_render[:-(right - size[0]), :]
            right = size[0]
        if top >= size[1]:
            arr_to_render = arr_to_render[:, :-(top - size[1])]
            top = size[1]

        # Render sprite
        out[left:right, bottom:top] = arr_to_render

    return array_to_string(add_borders(out))
