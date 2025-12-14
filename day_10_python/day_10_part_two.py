__author__ = "Maximilian Geitner"
__date__ = "10.12.2025"

from scipy.optimize import linprog
import numpy as np

def map_machine_description(text_input: str):
    parts = text_input.replace("[", "").replace("]", "")
    return list(map(lambda part: True if part == '#' else False, parts))

def map_button_descriptions(text_inputs: list[str]):
    buttons = []
    for text_input in text_inputs:
        parts = text_input.replace("(", "").replace(")", "").split(",")
        button_description = list(map(lambda part: int(part), parts))
        buttons.append(button_description)
    return buttons

def map_joltage_requirement_description(text_input: str):
    parts = text_input.replace("{", "").replace("}", "").split(",")
    return list(map(lambda part: int(part), parts))


# Idea: Use linear programming
# - Use amount button presses as minimization goal
# - formulate equations for each counter
def evaluate_machine(line_input: str):
    parts = line_input.split(" ")
    joltage_requirements = map_joltage_requirement_description(parts[-1])
    buttons = map_button_descriptions(parts[1:-1])

    c = [1] * len(buttons)
    A = []
    for button in buttons:
        button_values = [0] * len(joltage_requirements)
        for index in button:
            button_values[index] += 1
        A.append(button_values)
    A = np.array(A).transpose()
    b = joltage_requirements
    res = linprog(c, A_eq=A, b_eq=b, method='highs', integrality=[1] * len(buttons)) # only keep integer solutions
    return round(res.fun)

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            input_line_solution = evaluate_machine(line)

            solution += input_line_solution

    print("Solution Day 10 Part 2: ", solution)
