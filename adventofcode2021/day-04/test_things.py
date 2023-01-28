from main import Board


def test_board_draw():
    lines = [
        '22 13 17 11  0',
        '8  2 23  4 24',
        '21  9 14 16  7',
        '6 10  3 18  5',
        '1 12 20 15 19'
    ]
    board = Board.make(lines)

    assert board.draw(2) is False


def test_board_draw_whole_line():
    lines = [
        '22 13 17 11  0',
        '8  2 23  4 24',
        '21  9 14 16  7',
        '6 10  3 18  5',
        '1 12 20 15 19'
    ]
    board = Board.make(lines)

    assert board.draw(0) is False
    assert board.draw(2) is False
    assert board.draw(8) is False
    assert board.draw(23) is False
    assert board.draw(4) is False
    assert board.draw(24) is True

    undrawn = 22 + 13 + 17 + 11 + 21 + 9 + 14 + 16 + 7 + 6 + 10 + 3 + 18 + 5 + 1 + 12 + 20 + 15 + 19
    assert board.score() == undrawn * 24


def test_board_draw_whole_column():
    lines = [
        '22 13 17 11  0',
        '8  2 23  4 24',
        '21  9 14 16  7',
        '6 10  3 18  5',
        '1 12 20 15 19'
    ]
    board = Board.make(lines)

    assert board.draw(8) is False
    assert board.draw(22) is False
    assert board.draw(21) is False
    assert board.draw(6) is False
    assert board.draw(1) is True
