from main import parse_lines, Vector, draw_line, Point, Matrix

lines = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def test_parse_lines():
    parsed_lines = parse_lines(lines)

    assert len(parsed_lines) == len(lines)
    assert parsed_lines[0] == ((0, 9), (5, 9))


def test_draw_horizontal_line():
    v = Vector(a=Point(0, 0), b=Point(3, 0))
    line = sorted(draw_line(v))

    assert line == [(0, 0), (1, 0), (2, 0), (3, 0)]


def test_draw_horizontal_line_reversed():
    v = Vector(a=Point(3, 0), b=Point(0, 0))
    line = sorted(draw_line(v))

    assert line == [(0, 0), (1, 0), (2, 0), (3, 0)]


def test_draw_vertical_line():
    v = Vector(a=Point(1, 1), b=Point(1, 4))
    line = sorted(draw_line(v))

    assert line == [(1, 1), (1, 2), (1, 3), (1, 4)]


def test_draw_vertical_line_reversed():
    v = Vector(a=Point(1, 4), b=Point(1, 1))
    line = sorted(draw_line(v))

    assert line == [(1, 1), (1, 2), (1, 3), (1, 4)]


def test_draw_diagonal_up():
    v = Vector(a=Point(1, 1), b=Point(3, 3))
    line = sorted(draw_line(v))

    assert line == [(1, 1), (2, 2), (3, 3)]


def test_draw_diagonal_up_reversed():
    v = Vector(a=Point(3, 3), b=Point(1, 1))
    line = sorted(draw_line(v))

    assert line == [(1, 1), (2, 2), (3, 3)]


def test_draw_diagonal_down():
    v = Vector(a=Point(1, 3), b=Point(3, 1))
    line = sorted(draw_line(v))

    assert line == [(1, 3), (2, 2), (3, 1)]


def test_draw_diagonal_down_reversed():
    v = Vector(a=Point(3, 1), b=Point(1, 3))
    line = sorted(draw_line(v))

    assert line == [(1, 3), (2, 2), (3, 1)]

def test_matrix():
    m = Matrix()
    m[2, 9] = 3
    m[3, 3] += 1
    m[3, 3] += 1

    assert m[3, 3] == 2
    assert m.all_weighted_points() == [(Point(2, 9), 3), (Point(3, 3), 2)]
