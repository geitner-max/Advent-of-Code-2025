
__author__ = "Maximilian Geitner"
__date__ = "06.12.2025"


def process_number_line(line_input):
    current_input = ""
    output = []
    for char in line_input:
        if char == ' ':
            if current_input != "":
                output.append(int(current_input))
            current_input = ""
        else:
            current_input += char
    if current_input != "":
        output.append(int(current_input))
    return output

def process_operator_line(line_input: str, column_number_values):
    final_result = 0
    cur_index = 0
    # idea: Apply operator to numbers in each column
    for char in line_input:
        if char == '+':
            column_result = 0
            for column_number in column_number_values[cur_index]:
                column_result += column_number
            cur_index += 1
            final_result += column_result
        elif char == '*':
            column_result = 1
            for column_number in column_number_values[cur_index]:
                column_result *= column_number
            cur_index += 1
            final_result += column_result
    return final_result


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    # 1.) Read Input
    column_numbers = []
    is_first_line = True
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            if is_first_line:
                # 2.1) read first row with numbers and create data structure
                column_numbers = list(map(lambda num: [num], process_number_line(line)))
                is_first_line = False
            elif '+' in line or '*' in line:
                # 3.) find all operators in the last line
                solution = process_operator_line(line, column_numbers)
            else:
                # 2.2) read row with numbers and add to data structure
                output_numbers = process_number_line(line)
                for index, number in enumerate(output_numbers):
                    column_numbers[index].append(number)



    print("Solution Day 6 Part 1: ", solution)
