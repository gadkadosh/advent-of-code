def get_input(filename: str) -> list[str]:
    input = []
    with open(filename) as file:
        input = file.read().strip().split("\n")
    return input


def find_most_common(binary_bit: list[str]) -> str:
    only_ones = [x for x in binary_bit if x == "1"]
    ratio = len(only_ones) / len(binary_bit)
    if ratio == 0.5:
        return str(1)
    return str(round(ratio))


def binary_to_decimal(binary: str) -> int:
    result = [pow(2, i) * int(bit) for i, bit in enumerate(reversed(binary))]
    return sum(result)


def calc_power_consumption(diagnostics):
    line_length = len(diagnostics[0])
    result = []
    for i in range(line_length):
        current_bit = [line[i] for line in diagnostics]
        result.append(find_most_common(current_bit))

    binary_gamma_rate = "".join(result)
    binary_epsilon_rate = "".join(["0" if x == "1" else "1" for x in result])

    print(f"Binary Gamma rate: {binary_gamma_rate}")
    gamma_rate = binary_to_decimal(binary_gamma_rate)
    print(f"Decimal Gamma rate: {gamma_rate}")

    print(f"Binary Epsilon rate: {binary_epsilon_rate}")
    epsilon_rate = binary_to_decimal(binary_epsilon_rate)
    print(f"Decimal Epsilon rate: {epsilon_rate}")

    print(f"The power consumption of the submarine is: {gamma_rate * epsilon_rate}")


def calc_o2_gen_binary(diagnostics):
    line_length = len(diagnostics[0])

    for i in range(line_length):
        if len(diagnostics) == 1:
            break
        current_bit = [line[i] for line in diagnostics]
        most_common = find_most_common(current_bit)
        diagnostics = [bit for bit in diagnostics if bit[i] == most_common]
    return diagnostics[0]


def calc_co2_scrub_binary(diagnostics):
    line_length = len(diagnostics[0])

    for i in range(line_length):
        if len(diagnostics) == 1:
            break
        current_bit = [line[i] for line in diagnostics]
        least_common = "0" if find_most_common(current_bit) == "1" else "1"
        diagnostics = [line for line in diagnostics if line[i] == least_common]
    return diagnostics[0]


def calc_life_support_rate(diagnostics):

    o2_gen_binary = calc_o2_gen_binary(diagnostics)
    co2_scrub_binary = calc_co2_scrub_binary(diagnostics)

    print(f"Binary Oxygen Generator rate: {o2_gen_binary}")
    o2_gen_rating = binary_to_decimal(o2_gen_binary)
    print(f"Decimal Oxygen Generator rate: {o2_gen_rating}")

    print(f"Binary CO2 Scrubbing rate: {co2_scrub_binary}")
    co2_scrub_rating = binary_to_decimal(co2_scrub_binary)
    print(f"Decimal CO2 Scrubbing rate: {co2_scrub_rating}")

    print(
        f"The life support rating of the submarine is: {o2_gen_rating * co2_scrub_rating}"
    )


def main():
    diagnostics = get_input("./day3_input")

    print("Part One\n")
    calc_power_consumption(diagnostics)
    print("\nPart Two\n")
    calc_life_support_rate(diagnostics)


if __name__ == "__main__":
    main()
