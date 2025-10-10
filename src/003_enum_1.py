from enum import Enum, unique


@unique  # does not allow the same value in class like white = 255 and black = 255
class Color(Enum):
    red = (127, 0, 0)
    green = (127, 127, 255)
    blue = (0, 255, 0)

    # grey = 'grey'
    # white = 255
    # black = [0, 0, 0]

    white = 255  # exist attribute
    # black = 255  # black becomes alias for white WITHOUT @unique


class Figure(Enum):
    RECT = 0
    TRIANGLE = 1
    CIRCLE = 3

    # class Enum can contain methods
    def describe(self):
        if self == Figure.RECT:
            return 'Rectangle'
        elif self == Figure.TRIANGLE:
            return 'Triangle'
        elif self == Figure.CIRCLE:
            return 'Cicle'

        return 'Unknown'


def descr_color():
    color = Color.red

    print(color)        # Color.red
    print(type(color))  # <enum 'Color'>
    print(color.name)   # red
    print(color.value)  # (127, 0, 0)

    print(Color.white)  # Color.white
    # print(Color.black)  # Color.white

    pk = Color['red']
    print(pk.value)     # (127, 0, 0)

    for p in Color:
        print(f"{p.name} = {p.value}")


def fig_per(*args, fig: Figure = Figure.RECT):
    if fig == Figure.RECT:
        return 2 * (args[0] + args[1])
    if fig == Figure.TRIANGLE:
        return args[0] + args[1] + args[2]
    if fig == Figure.CIRCLE:
        return 2 * 3.1415 * args[0]

    return -1  # Unknown figure


def descr_figure():
    print(fig_per(10, 20))                        # 60
    print(fig_per(10, 20, fig=0))                 # -1
    print(fig_per(1, 2, 3, fig=Figure.TRIANGLE))  # 6
    print(fig_per(7, fig=Figure.CIRCLE))          # 43.981

    p = Figure.TRIANGLE
    print(p.describe())                           # Triangle


if __name__ == '__main__':
    descr_color()
    print("\n################\n")
    descr_figure()
