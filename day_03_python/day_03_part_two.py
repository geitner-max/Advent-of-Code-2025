
__author__ = "Maximilian Geitner"
__date__ = "03.12.2025"

def find_highest_digit(line_input, cur_index, remaining_digits):
    highest_found_digit = 0
    highest_index = cur_index
    for i in range(cur_index, len(line_input) - remaining_digits + 1):
        if int(line_input[i]) > highest_found_digit:
            highest_found_digit = int(line_input[i])
            highest_index = i
    return highest_found_digit, highest_index

def find_highest_voltage(line_input: str):
    cur_seq = ''
    remaining_digits = 12
    cur_min_index = 0
    while len(cur_seq) < 12:
        # add next highest digit
        highest_digit, index_digit = find_highest_digit(line_input, cur_min_index, remaining_digits)
        cur_seq += str(highest_digit)
        remaining_digits -= 1
        cur_min_index = (index_digit + 1)
    return int(cur_seq)

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    # 1.) Read Input
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            # 2.) Improve solution from first part:
            #   find most suitable digit (highest digit) in a specific valid range from the given input row
            solution += find_highest_voltage(line)


    print("Solution Day 3 Part 2: ", solution)
