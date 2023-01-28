
def main():
    input_data = fetch_input("input.txt")
    print(counter(parse_input(input_data)))


def fetch_input(fn):
    with open(fn) as fh:
        return fh.read()

def parse_input(lines):
    return [int(n.strip()) for n in lines.strip().split("\n")]

def counter(numbers):
    greater = 0
    last = numbers[0]
    for number in numbers[1:]:
        if last < number:
            greater += 1
        last = number
    return greater


if __name__ == "__main__":
    main()
