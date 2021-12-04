from functools import reduce
from copy import deepcopy


def get_input():
    lines = []
    with open("./day3_input", "r") as file:
        lines = file.read().splitlines()

    return [list(line) for line in lines]


def traverse_map(original_map, x_change, y_change):
    map = deepcopy(original_map)
    encounters = 0
    bottom = len(map)
    right_limit = len(map[0])

    x = 0
    y = 0

    while y < bottom:
        if x >= right_limit:
            x -= right_limit
        position = map[y][x]
        if position == "#":
            encounters += 1
            map[y][x] = "X"
        else:
            map[y][x] = "O"
        x += x_change
        y += y_change

    draw_map(map)
    return encounters


def draw_map(map):
    print("\n".join(["".join(line) for line in map]))


def main():
    map = get_input()
    encounters = traverse_map(map, 3, 1)
    print("Entcountered on the way {} trees.".format(encounters))

    slopes = [
        {"x": 1, "y": 1},
        {"x": 3, "y": 1},
        {"x": 5, "y": 1},
        {"x": 7, "y": 1},
        {"x": 1, "y": 2},
    ]

    all_slopes_encounters = [
        traverse_map(map, slope["x"], slope["y"]) for slope in slopes
    ]
    print("All encounters: {}".format(all_slopes_encounters))
    product = reduce(lambda acc, x: acc * x, all_slopes_encounters)
    print(product)


if __name__ == "__main__":
    main()
