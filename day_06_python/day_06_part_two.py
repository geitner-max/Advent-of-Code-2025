__author__ = "Maximilian Geitner"
__date__ = "06.12.2025"


def solve_problem(initial_input):
    final_result = 0
    lines_with_numbers = len(initial_input) - 1
    # 2.1) create segments that belong together
    # Segments can be identified by index of operator to predecessor index of the next operator
    columns_with_operator = []
    for index_line, char in enumerate(initial_input[-1]):
        if char == '+' or char == '*':
            columns_with_operator.append(index_line)
    max_line_count = max(map(lambda x: len(x), initial_input))
    columns_with_operator.append(max_line_count + 1) # add additional marker for the last segment

    # 2.2) Evaluate each segment individually
    for segment_index in range(len(columns_with_operator) - 1):
        operator = initial_input[-1][columns_with_operator[segment_index]]
        segment_start = columns_with_operator[segment_index]
        segment_end = columns_with_operator[segment_index + 1] - 1
        numbers_segment = []
        # 2.2.1) Build numbers which are listed in each column
        for selected_col_index in range(segment_start, segment_end):
            number_input = ""
            for row_index in range(lines_with_numbers):
                if selected_col_index < len(initial_input[row_index]):
                    number_input += initial_input[row_index][selected_col_index]
            numbers_segment.append(int(number_input.replace(" ", "")))
        # 2.2.2) Evaluate operator for current segment and compute result for this segment
        if operator == "+":
            segment_result = 0
        else:
            segment_result = 1
        for number in numbers_segment:
            if operator == "+":
                segment_result += number
            else:
                segment_result *= number
        final_result += segment_result
    return final_result


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    # 1.) Read Input and collect complete input
    column_numbers = []
    is_first_line = True
    initial_lines = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            initial_lines.append(line)
    # 2.) Build numbers and compute results for each column
    solution = solve_problem(initial_lines)

    print("Solution Day 6 Part 2: ", solution)
