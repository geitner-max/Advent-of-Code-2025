__author__ = "Maximilian Geitner"
__date__ = "10.12.2025"


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


def apply_button(machine_state: list[bool], button: list[int]):
    next_state = machine_state.copy()
    for index in button:
        next_state[index] = not next_state[index]
    return next_state


def evaluate_machine(line_input: str):
    parts = line_input.split(" ")
    target_machine_state = map_machine_description(parts[0])
    joltage_requirements = map_joltage_requirement_description(parts[-1])
    buttons = map_button_descriptions(parts[1:-1])
    initial_machine_state = [False] * len(target_machine_state)
    states = [initial_machine_state]
    presses_count = 0

    to_evaluate = [initial_machine_state]
    # Idea: apply all button presses on currently known states until the goal state is found
    while len(to_evaluate) > 0:
        next_to_evaluate = []
        presses_count += 1
        for state in to_evaluate:
            for button in buttons:
                next_state = apply_button(state, button)
                if next_state not in states:
                    states.append(next_state)
                    if next_state == target_machine_state:
                        return presses_count
                    next_to_evaluate.append(next_state)
        to_evaluate = next_to_evaluate
    return 0


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    # '.'=off, '#'=on
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            input_line_solution = evaluate_machine(line)
            solution += input_line_solution

    print("Solution Day 10 Part 1: ", solution)
