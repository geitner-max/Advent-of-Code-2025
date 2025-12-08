__author__ = "Maximilian Geitner"
__date__ = "07.12.2025"

from functools import reduce


# apply one split option to the current scenario based on the row data and how it splits the beam
def compute_row_tachyon_split(line_input, tachyons_prev_row_indices, splits_left, splits_right):
    next_tachyon_column_indices = [False] * len(tachyons_prev_row_indices)
    for column_index in range(len(tachyons_prev_row_indices)):
        if line_input[column_index] == '^' and tachyons_prev_row_indices[column_index]:
            # left split
            if column_index >= 1 and splits_left:
                next_tachyon_column_indices[column_index - 1] = True
            # right split
            if column_index + 1 < len(line_input) and splits_right:
                next_tachyon_column_indices[column_index + 1] = True
        else:
            if tachyons_prev_row_indices[column_index]:
                next_tachyon_column_indices[column_index] = True
    return next_tachyon_column_indices


# Idea: Apply both split options to all scenarios evaluated until the previous row and compute the scenarios
#       Also track the occurrence count for each scenario after evaluating all options
def compute_row_combinations(line_input, tachyons_prev_row_scenarios, prev_scenarios_occurrences):
    next_combinations = []
    next_scenario_occurrences = []
    for (index, tachyons_prev_row_scenario) in enumerate(tachyons_prev_row_scenarios):
        prev_scenario_occurrences = prev_scenarios_occurrences[index]
        scenario_left_split_only = compute_row_tachyon_split(line_input, tachyons_prev_row_scenario, True, False)
        scenario_right_split_only = compute_row_tachyon_split(line_input, tachyons_prev_row_scenario, False, True)
        if scenario_left_split_only == scenario_right_split_only:
            # no split with different scenario outcome occurred, only add one scenario to results
            if scenario_left_split_only not in next_combinations:
                next_combinations.append(scenario_left_split_only)
                next_scenario_occurrences.append(prev_scenario_occurrences)
            else:
                next_scenario_occurrences[
                    next_combinations.index(scenario_left_split_only)] += prev_scenario_occurrences
        else:
            if scenario_left_split_only not in next_combinations:
                next_combinations.append(scenario_left_split_only)
                next_scenario_occurrences.append(prev_scenario_occurrences)
            else:
                next_scenario_occurrences[
                    next_combinations.index(scenario_left_split_only)] += prev_scenario_occurrences
            if scenario_right_split_only not in next_combinations:
                next_combinations.append(scenario_right_split_only)
                next_scenario_occurrences.append(prev_scenario_occurrences)
            else:
                next_scenario_occurrences[
                    next_combinations.index(scenario_left_split_only)] += prev_scenario_occurrences
    return next_combinations, next_scenario_occurrences


if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    column_numbers = []
    is_first_line = True
    tachyon_column_scenarios = []
    scenario_occurrences = [1]
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            # 1.) Initialize first scenario with starting position
            #     One scenario describes where the tachyon beams are located at a given row
            if is_first_line:
                start_pos = line.find('S')
                tachyon_column_indices = [False] * len(line)
                tachyon_column_indices[start_pos] = True
                tachyon_column_scenarios = [tachyon_column_indices]
                is_first_line = False
            else:
                # 2.)   For all currently known scenario, apply both beam split options in a row (left or right split)
                #       Then, update count for all possible scenarios after applying one row
                tachyon_column_scenarios, scenario_occurrences = compute_row_combinations(line,
                                                                                          tachyon_column_scenarios,
                                                                                          scenario_occurrences)

    solution = reduce(lambda x, y: x + y, scenario_occurrences)

    print("Solution Day 6 Part 2: ", solution)
