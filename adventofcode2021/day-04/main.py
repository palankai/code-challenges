

def main():
    draws, boards = parse_file(read_file("input.txt"))
    for number in draws:

        for board in boards:
            if board.winner:
                continue
            winner = board.draw(number)
            if winner:
                print(board.score())


def read_file(fn):
    with open(fn) as fh:
        return fh.read().splitlines()


def parse_file(lines):
    draw = [int(n.strip()) for n in lines[0].strip().split(",")]
    boards = []
    buffer = []
    for line in lines[2:]:
        if not line.strip():
            boards.append(Board.make(buffer))
            buffer = []
        else:
            buffer.append(line.strip())
    if boards:
        boards.append(Board.make(buffer))
    return draw, boards


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0])
        self.drawn = []
        self.winner = False

    @classmethod
    def make(cls, lines):
        data = [[[int(n), False] for n in line.split()] for line in lines]
        return cls(data)

    def draw(self, number):
        self.drawn.append(number)
        for r, row in enumerate(self.rows):
            for c, rec in enumerate(row):
                if rec[0] == number:
                    rec[1] = True
        for row in self.rows:
            if all(map(lambda e: e[1], row)):
                self.winner = True
                return True

        for c in range(self.width):
            column = []
            for r in range(self.height):
                column.append(self.rows[r][c][1])
            if all(column):
                self.winner = True
                return True
        return False

    def score(self):
        sum = 0
        for row in self.rows:
            for (number, drawn) in row:
                if not drawn:
                    sum += number
        return sum * self.drawn[-1]


if __name__ == '__main__':
    main()
