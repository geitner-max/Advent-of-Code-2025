
__author__ = "Maximilian Geitner"
__date__ = "05.12.2025"


def is_fresh_ingredient(ingredient_id, ingredient_ranges):
    for (start_index, end_index) in ingredient_ranges:
        if start_index <= ingredient_id <= end_index:
            return True
    return False

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
                # 3.) check for fresh ingredients
                is_fresh = is_fresh_ingredient(int(line), fresh_ingredients)
                if is_fresh:
                    solution += 1
    print("Solution Day 5 Part 1: ", solution)
