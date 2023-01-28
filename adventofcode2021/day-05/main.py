import itertools
from collections import namedtuple, defaultdict
from typing import Tuple, List

Point = namedtuple("Coordinate", ["x", "y"])
Vector = namedtuple("Vector", ["a", "b"])
Line = List[Point]


def main(fh):
    parsed = parse_lines(read_lines(fh))
    m = Matrix()
    for v in parsed:
        for p in draw_line(v):
            m[p] += 1
    counter = 0
    for p, c in m.all_weighted_points():
        if c >= 2:
            counter += 1
    print(counter)


def read_lines(fn):
    with open(fn) as fh:
        return [l.strip() for l in fh.read().split("\n") if l.strip()]


def parse_lines(lines):
    parsed_lines = []
    for line in lines:
        a, b = line.split(" -> ")
        parsed_lines.append((
            Vector(_parse_coordinate(a), _parse_coordinate(b))
        ))
    return parsed_lines


def _parse_coordinate(coord: str) -> Point:
    x, y = coord.split(",")
    return Point(int(x), int(y))


def draw_line(v: Vector) -> Line:
    if v.a.y == v.b.y:
        if v.a.x < v.b.x:
            return [(x, v.a.y) for x in range(v.a.x, v.b.x + 1)]
        else:
            return [(x, v.a.y) for x in range(v.b.x, v.a.x + 1)]
    if v.a.x == v.b.x:
        if v.a.y < v.b.y:
            return [(v.a.x, y) for y in range(v.a.y, v.b.y + 1)]
        else:
            return [(v.a.x, y) for y in range(v.b.y, v.a.y + 1)]
    if abs(v.a.x - v.b.x) == abs(v.a.y - v.b.y):
        if v.a.x < v.b.x and v.a.y < v.b.y:
            return [(v.a.x+i, v.a.y+i) for i in range(abs(v.a.y - v.b.y) + 1)]
        if v.a.x < v.b.x and v.a.y > v.b.y:
            return [(v.a.x + i, v.a.y - i) for i in range(abs(v.a.y - v.b.y) + 1)]
        if v.a.x > v.b.x and v.a.y > v.b.y:
            return [(v.b.x + i, v.b.y + i) for i in range(abs(v.a.y - v.b.y) + 1)]
        if v.a.x > v.b.x and v.a.y < v.b.y:
            return [(v.b.x + i, v.b.y - i) for i in range(abs(v.a.y - v.b.y) + 1)]
    assert False, f"Found non expected line f{v}"


class Matrix:
    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(lambda: 0))

    def __getitem__(self, item: Point):
        return self.points[item[0]][item[1]]

    def __setitem__(self, item: Point, value: int):
        self.points[item[0]][item[1]] = value

    def all_weighted_points(self):
        weighted_points = []
        for x, points in self.points.items():
            for y, value in points.items():
                weighted_points.append((Point(x, y), value))
        return sorted(weighted_points, key=lambda v: v[1], reverse=True)


if __name__ == '__main__':
    main("input.txt")
