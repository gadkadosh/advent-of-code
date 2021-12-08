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


def cycle_day(state):
    new_state = create_state_table()

    new_state[6] = state[0]
    new_state[8] = state[0]
    for i in range(1, AGES):
        new_state[i - 1] += state[i]

    return new_state


def create_state_table():
    state = []
    for _ in range(AGES):
        state.append(0)
    return state


def count_fish(state):
    sum = 0
    for i in state:
        sum += i
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
