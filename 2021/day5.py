RawInput = list[str]
Pos = tuple[int, ...]
ParsedInput = list[tuple[Pos, ...]]
Diagram = list[list[int]]


def get_input(filename: str) -> RawInput:
    input = []
    with open(filename) as file:
        input = file.read().strip().splitlines()

    return input


def parse_input(input: list[str]) -> ParsedInput:
    lines = [
        tuple([tuple([int(x) for x in pos.split(",")]) for pos in line.split(" -> ")])
        for line in input
    ]
    return lines


def create_diagram(input: ParsedInput) -> Diagram:
    max_x = max([max([coord[0] for coord in line]) for line in input])
    max_y = max([max([coord[1] for coord in line]) for line in input])

    diagram = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    return diagram


def mark_simple_lines(diagram: Diagram, input: ParsedInput):
    for coordinates in input:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        # horizonal lines
        if x1 == x2:
            r = None
            if y2 > y1:
                r = range(y1, y2 + 1)
            else:
                r = range(y2, y1 + 1)
            for y in r:
                diagram[y][x1] += 1
        # vertical lines
        elif y1 == y2:
            r = None
            if x2 > x1:
                r = range(x1, x2 + 1)
            else:
                r = range(x2, x1 + 1)
            for x in r:
                diagram[y1][x] += 1

    return diagram


def mark_diagonals(diagram, input):
    for coordinates in input:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if abs(x2 - x1) != abs(y2 - y1):
            continue
        # top left to bottom right
        if x2 > x1 and y2 > y1:
            add = 0
            while x1 + add <= x2 and y1 + add <= y2:
                diagram[y1 + add][x1 + add] += 1
                add += 1
        # bottom right to top left
        if x2 < x1 and y2 < y1:
            add = 0
            while x1 - add >= x2 and y1 - add >= y2:
                diagram[y1 - add][x1 - add] += 1
                add += 1
        # top right to bottom left
        if x2 < x1 and y2 > y1:
            add = 0
            while x1 - add >= x2 and y1 + add <= y2:
                diagram[y1 + add][x1 - add] += 1
                add += 1
        # top right to bottom left
        if x2 > x1 and y2 < y1:
            add = 0
            while x1 + add <= x2 and y1 - add >= y2:
                diagram[y1 - add][x1 + add] += 1
                add += 1

    return diagram


def print_diagram(diagram: Diagram):
    diagram_string = [[str(x) if x > 0 else "." for x in line] for line in diagram]
    diagram_string = "\n".join(["".join(line) for line in diagram_string])
    print(diagram_string)


def count_dangerous_areas(diagram, threshold):
    count = 0
    for line in diagram:
        for point in line:
            if point >= threshold:
                count += 1
    return count


def main():
    input = parse_input(get_input("./day5_input"))

    diagram = create_diagram(input)

    diagram = mark_simple_lines(diagram, input)
    dangerous_areas = count_dangerous_areas(diagram, 2)
    print("Part one")
    print(
        f"At {dangerous_areas} points at least two lines overlap (only horizonal and verical considered)"
    )

    diagram = mark_diagonals(diagram, input)
    dangerous_areas = count_dangerous_areas(diagram, 2)
    print("\nPart two")
    print(
        f"At {dangerous_areas} points at least two lines overlap (including 45deg diagonals)"
    )
    # print_diagram(diagram)


if __name__ == "__main__":
    main()
