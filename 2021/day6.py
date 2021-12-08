FishState = list[int]

AGES = 9  # possible ages are 0 - 8 days


def get_fish_state(filename: str) -> FishState:
    state = []
    with open(filename) as file:
        state = file.read().strip().split(",")

    return [int(x) for x in state]


# works but extremely inefficient, probably too much memory
# see the other solution using a table of count of fish of each age.
def calc_state_after(old_state: FishState, iterations: int) -> FishState:
    middle_state = old_state[:]

    for _ in range(iterations):
        new_state = []
        for fish in middle_state[:]:
            if fish == 0:
                new_state.append(6)
                new_state.append(8)
            else:
                new_state.append(fish - 1)
        middle_state = new_state[:]

    return middle_state


def cycle_day(table):
    new_table = {}
    for i in range(10):
        new_table[i] = 0

    for i in table:
        if i == 0:
            new_table[6] = table[i]
            new_table[8] = table[i]
        if i > 0:
            new_table[i - 1] = new_table[i - 1] + table[i]

    return new_table


def create_state_table():
    table = {}
    for i in range(AGES):
        table[i] = 0
    return table


def count_fish(table):
    sum = 0
    for i in table:
        sum += table[i]
    return sum


def main():
    initial_state = get_fish_state("./day6_input")

    # This implementation is too slow - most probably it needs too much memory
    # iterations = 80
    # new_state = calc_state_after(initial_state, iterations)
    # print("Part one")
    # print(f"After {iterations} days there are {len(new_state)} lanternfish")

    # iterations = 120
    # new_state = calc_state_after(initial_state, iterations)
    # print("\nPart two")
    # print(f"After {iterations} days there are {len(new_state)} lanternfish")

    state_table = create_state_table()
    for i in initial_state:
        state_table[i] += 1
    days = 80
    for i in range(days):
        state_table = cycle_day(state_table)
    print("Part one")
    print(f"After {days} days there are {count_fish(state_table)} lanternfish")

    state_table = create_state_table()
    for i in initial_state:
        state_table[i] += 1
    days = 256
    for i in range(days):
        state_table = cycle_day(state_table)
    print("Part one")
    print(f"After {days} days there are {count_fish(state_table)} lanternfish")


if __name__ == "__main__":
    main()
