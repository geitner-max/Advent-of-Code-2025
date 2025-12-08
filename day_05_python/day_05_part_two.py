__author__ = "Maximilian Geitner"
__date__ = "05.12.2025"


def aggregate_ingredient_ranges(ingredient_ranges):
    # idea: Find overlap between two intervals and merge them
    for i in range(len(ingredient_ranges)):
        for j in range(i + 1, len(ingredient_ranges)):
            id_first_start = ingredient_ranges[i][0]
            id_first_end = ingredient_ranges[i][1]
            id_second_start = ingredient_ranges[j][0]
            id_second_end = ingredient_ranges[j][1]
            if id_second_start <= id_first_end <= id_second_end:
                # merge ingredient ranges
                return ingredient_ranges[0:i] + ingredient_ranges[i + 1: j] + ingredient_ranges[
                    j + 1:len(ingredient_ranges)] + [
                           (min(id_first_start, id_second_start), max(id_first_end, id_second_end))], True
            elif id_first_start <= id_second_end <= id_first_end:
                return ingredient_ranges[0:i] + ingredient_ranges[i + 1: j] + ingredient_ranges[
                    j + 1:len(ingredient_ranges)] + [
                           (min(id_first_start, id_second_start), max(id_first_end, id_second_end))], True
    return ingredient_ranges, False


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    # 1.) Read Input
    level_input = []

    fresh_ingredients = []
    state = 0
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            level_input.append(line)
            if line == "":
                state = 1

            elif state == 0:
                # 2.) read ingredient range
                line_parts = line.split("-")
                first_index = int(line_parts[0])
                second_index = int(line_parts[1])
                fresh_ingredients.append((first_index, second_index))
            else:
                pass
    # 3.) aggregate ingredient ranges
    while True:
        fresh_ingredients, has_changed = aggregate_ingredient_ranges(fresh_ingredients)
        if not has_changed:
            break
    for ingredient_range in fresh_ingredients:
        solution = solution + (ingredient_range[1] - ingredient_range[0]) + 1
    print("Solution Day 5 Part 2: ", solution)
