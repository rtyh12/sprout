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
                                (x_axis_numbers.shape[1], 0),
                            ),
                            'constant',
                            constant_values=(' '))

    arr = np.concatenate([y_axis_numbers, arr], axis=0)

    return arr


def array_to_string(arr: np.ndarray) -> str:
    out = '```'

    for y in reversed(range(arr.shape[1])):
        for x in range(arr.shape[0]):
            out += arr[x, y]
        out += '\n'

    out += '```'

    return out


def render() -> None:
    size = (100, 15)
    out = np.zeros(size, np.str_)
    for x in range(size[0]):
        col = np.zeros(size[1], np.str_)
        plant_height = 5
        col[:plant_height] = '|'
        col[plant_height:] = '-'
        out[x, :] = col
    return array_to_string(add_borders(out))
