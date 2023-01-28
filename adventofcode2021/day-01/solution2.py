
def main():
    input_data = fetch_input("input.txt")
    print(sliding_counter(parse_input(input_data)))


def fetch_input(fn):
    with open(fn) as fh:
        return fh.read()

def parse_input(lines):
    return [int(n.strip()) for n in lines.strip().split("\n")]

def sliding_counter(numbers):
    greater = 0
    for i in range(3, len(numbers)+1):
        if i > 3:
            a = numbers[i-4:i-1]
            b = numbers[i-3:i]
            print(i, a, b, sum(a), sum(b))
            if sum(a) < sum(b):
                greater += 1

    return greater



if __name__ == "__main__":
    main()
