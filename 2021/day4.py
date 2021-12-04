Cell = tuple[str, bool]
Board = list[list[str]]
ParsedBoard = list[list[Cell]]
BoardsList = list[ParsedBoard]


def parse_input(filename: str):
    input = []
    with open(filename) as file:
        input = file.read().strip().split("\n\n")

    drawn_numbers = input[0].split(",")
    boards = [b.split("\n") for b in input[1:]]
    return drawn_numbers, parse_boards(boards)


def parse_board_line(line: str):
    parsed = []
    while len(line) > 0:
        parsed.append((line[:3].strip(), False))
        line = line[3:]
    return parsed


def parse_boards(boards: Board):
    all_parsed = []
    for board in boards:
        parsed_board = []
        for line in board:
            parsed_board.append(parse_board_line(line))
        all_parsed.append(parsed_board)
    return all_parsed


def check_won(board: ParsedBoard) -> bool:
    for line in board:
        if all([cell[1] for cell in line]):
            return True

    for i in range(len(board[0])):
        col = [line[i] for line in board]
        if all([cell[1] for cell in col]):
            return True

    return False


def mark_drawn_numbers(board: ParsedBoard, number: str) -> ParsedBoard:
    for i, line in enumerate(board):
        for j, cell in enumerate(line):
            if cell[0] == number:
                board[i][j] = (number, True)
    return board


def calculate_score(board: ParsedBoard, final_number: int) -> int:
    total = 0
    for line in board:
        total += sum([int(cell[0]) for cell in line if not cell[1]])

    return total * final_number


# Part one
def win_first(drawn_numbers: list[str], boards: BoardsList):
    for num in drawn_numbers:
        for i, board in enumerate(boards):
            board = mark_drawn_numbers(board, num)
            if check_won(board):
                print(f"Board number {i + 1} won first!")
                print_results(num, board, i)
                return


# Part two
def let_him_win(drawn_numbers: list[str], boards: BoardsList):
    won_boards = []
    for num in drawn_numbers:
        for i, board in enumerate(boards):
            if i in won_boards:
                continue
            board = mark_drawn_numbers(board, num)
            if check_won(board):
                won_boards.append(i)
                if len(won_boards) != len(boards):
                    continue
                print(f"Last board to win is {i + 1}!")
                print_results(num, board, i)
                return


def print_results(num: str, board: ParsedBoard, i: int):
    print(f"Last number was: {num}")
    score = calculate_score(board, int(num))
    print(f"Final score for board {i + 1}: {score}")


def main():
    drawn_numbers, boards = parse_input("./day4_input")

    print("Part one\n")
    win_first(drawn_numbers, boards)
    print("\nPart two\n")
    let_him_win(drawn_numbers, boards)


if __name__ == "__main__":
    main()
