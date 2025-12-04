
__author__ = "Maximilian Geitner"
__date__ = "04.12.2025"


def check_row(complete_input, index_row: int, index_col: int):
    if index_row < 0 or index_row >= len(complete_input):
        return 0
    paper_roll_count = 0
    for i in range(index_col - 1, index_col + 2):
        if 0 <= i < len(complete_input[index_row]):
            if complete_input[index_row][i] == '@':
                paper_roll_count = paper_roll_count + 1
    return paper_roll_count

def check_tile(complete_input,  index_row: int, index_col: int):
    neighbor_count = check_row(complete_input, index_row - 1, index_col) + check_row(complete_input, index_row, index_col) + check_row(complete_input, index_row + 1, index_col) - 1
    if index_row == 7 and index_col == 0:
        print(index_row, index_col, neighbor_count)
    return neighbor_count < 4 and complete_input[index_row][index_col] == '@'

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    # 1.) Read Input
    level_input = []

    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            level_input.append(line)

    # 2.) Evaluate neighbor count for each tile and count paper rolls with fewer than four neighbors
    for index_c, tile in enumerate(line):
        for index_r, line in enumerate(level_input):
            is_accessible = check_tile(level_input, index_r, index_c)
            if is_accessible:
                solution = solution + 1

    print("Solution Day 4 Part 1: ", solution)
