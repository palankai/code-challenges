
def main():
    input_data = fetch_input("input.txt")
    movements = parse_movements(input_data)
    horizontal, depth = calculate_position(movements)
    print(f'{horizontal} x {depth} = {horizontal*depth}')

def fetch_input(fn):
    with open(fn) as fh:
        return fh.read()

def parse_movements(lines):
    parsed = []
    for line in lines.strip().split("\n"):
        dir, num = line.strip().split(" ")
        parsed.append((dir, int(num)))
    return parsed

def calculate_position(movements):
    horizontal = 0
    depth = 0
    for direction, number in movements:
        if direction == "forward":
            horizontal += number
        if direction == "down":
            depth += number
        if direction == "up":
            depth -= number
    return horizontal, depth




if __name__ == "__main__":
    main()
