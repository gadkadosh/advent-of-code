from functools import reduce


def get_input(filename: str):
    input = []
    with open(filename) as file:
        input = [line.split(" ") for line in file.read().strip().split("\n")]
    return input


def steps_loop(steps):
    horizontal = 0
    depth = 0

    for step in steps:
        if step[0] == "forward":
            horizontal += int(step[1])
        elif step[0] == "down":
            depth += int(step[1])
        elif step[0] == "up":
            depth -= int(step[1])
    return horizontal, depth


def sum(a, b):
    return a + b


def steps_reduce(steps):
    horizontal = [int(step[1]) for step in steps if step[0] == "forward"]
    up = [int(step[1]) for step in steps if step[0] == "up"]
    down = [int(step[1]) for step in steps if step[0] == "down"]
    # combine both in one step
    depth = [
        int(step[1]) if step[0] == "down" else -int(step[1])
        for step in steps
        if step[0] in ["up", "down"]
    ]

    horizontal = reduce(sum, horizontal)
    up = reduce(sum, up)
    down = reduce(sum, down)
    depth = reduce(sum, depth)

    return horizontal, depth


def aim_loop(steps):
    aim = 0
    horizontal = 0
    depth = 0

    for step in steps:
        if step[0] == "forward":
            horizontal += int(step[1])
            depth += aim * int(step[1])
        elif step[0] == "up":
            aim -= int(step[1])
        elif step[0] == "down":
            aim += int(step[1])

    return horizontal, depth


# This idea didn't pan out much :)
def aim_reduce(steps):
    class SubmarineState:
        def __init__(self):
            self.aim = 0
            self.horizontal = 0
            self.depth = 0

    def reduce_func(acc, step):
        if step[0] == "forward":
            acc.horizontal += int(step[1])
            acc.depth += acc.aim * int(step[1])
        elif step[0] == "up":
            acc.aim -= int(step[1])
        elif step[0] == "down":
            acc.aim += int(step[1])

        return acc

    final = reduce(reduce_func, steps, SubmarineState())
    return final.horizontal, final.depth


def part_one(steps):
    horizontal, depth = steps_loop(steps)
    print(f"Horizontal position times final depth: {horizontal * depth}")

    horizontal, depth = steps_reduce(steps)
    print(f"Horizontal position times final depth: {horizontal * depth}")


def part_two(steps):
    horizontal = 0
    depth = 0

    horizontal, depth = aim_loop(steps)
    print(f"Horizontal position times final depth: {horizontal * depth}")

    horizontal, depth = aim_reduce(steps)
    print(f"Horizontal position times final depth: {horizontal * depth}")


def main():
    steps = get_input("./day2_input")

    print("Part one\n")
    part_one(steps)

    print("\nPart two\n")
    part_two(steps)


if __name__ == "__main__":
    main()
