
__author__ = "Maximilian Geitner"
__date__ = "03.12.2025"


def find_highest_voltage(line_input: str):
    highest_voltage = 0
    for i in range(len(line_input)):
        for j in range(i + 1, len(line_input)):
            voltage = int(line_input[i] + line_input[j])
            if voltage > highest_voltage:
                highest_voltage = voltage
    return highest_voltage

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

            # 2.) check every combination of two batteries and find the highest value per input row
            solution += find_highest_voltage(line)

    print("Solution Day 3 Part 1: ", solution)
