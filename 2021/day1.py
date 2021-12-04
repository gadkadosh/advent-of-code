def get_input(filename):
    input: list[int] = []
    with open(filename) as file:
        input = [int(i) for i in file.read().strip().split("\n")]
    return input


def has_increased(data):
    def inner(val):
        i, d = val
        return i != 0 and d > data[i - 1]

    return inner


def increased_comprehension(depths):
    return [d for i, d in enumerate(depths) if i != 0 and d > depths[i - 1]]


def increased_filter(depths):
    return list(filter(has_increased(depths), enumerate(depths)))


def increased_loop(depths):
    counter = 0
    for val in enumerate(depths):
        i, d = val
        if i != 0 and d > depths[i - 1]:
            counter += 1
    return counter


def part_one(depths):
    increased = increased_comprehension(depths)
    print(f"The number of times a depth measurement increases is: {len(increased)}")

    increased = increased_filter(depths)
    print(f"The number of times a depth measurement increases is: {len(increased)}")

    increased = increased_loop(depths)
    print(f"The number of times a depth measurement increases is: {increased}")


def part_two(depths):
    sliding_windows = [
        d + depths[i - 1] + depths[i - 2]
        for i, d in enumerate(depths)
        if 2 <= i <= len(depths) - 1
    ]

    increased = increased_comprehension(sliding_windows)
    print(f"The number of times a depth measurement increases is: {len(increased)}")

    increased = increased_filter(sliding_windows)
    print(f"The number of times a depth measurement increases is: {len(increased)}")

    increased = increased_loop(sliding_windows)
    print(f"The number of times a depth measurement increases is: {increased}")


def main():
    depths = get_input("./day1_input")

    print("Part one\n")
    part_one(depths)
    print("\nPart two\n")
    part_two(depths)


if __name__ == "__main__":
    main()
