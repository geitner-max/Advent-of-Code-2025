
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
    return neighbor_count < 4 and complete_input[index_row][index_col] == '@'

def perform_one_removal_procedure(complete_input):
    next_complete_input = []
    has_removed_paper_roll_in_step = False
    removal_count = 0
    for index_r, line in enumerate(complete_input):
        next_input = ''
        for index_c, tile in enumerate(complete_input):
            is_accessible = check_tile(complete_input, index_r, index_c)
            if is_accessible:
                has_removed_paper_roll_in_step = True
                next_input += '.'
                removal_count += 1
            else:
                next_input += complete_input[index_r][index_c]
        next_complete_input.append(next_input)
    return next_complete_input, has_removed_paper_roll_in_step, removal_count

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

    # 2.) Iteratively remove accessible paper rolls until no paper rolls can be removed
    while True:
        level_input, has_removed_paper_roll, count = perform_one_removal_procedure(level_input)
        solution += count
        if not has_removed_paper_roll:
            break

    print("Solution Day 4 Part 2: ", solution)
