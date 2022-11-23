from math import atan2, degrees


Point = tuple[float, float]


def all_equal(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)


def get_angle(x: Point, y: Point) -> float:
    return degrees(atan2(y[1] - x[1], y[0] - x[0]))
