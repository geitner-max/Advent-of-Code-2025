__author__ = "Maximilian Geitner"
__date__ = "09.12.2025"


def rectangle_intersects(rect_1, rect_2):
    rect_1_x, rect_1_y, rect_1_w, rect_1_h = rect_1
    rect_2_x, rect_2_y, rect_2_w, rect_2_h = rect_2
    if rect_1_x >= rect_2_x + rect_2_w:
        return False
    elif rect_1_x + rect_1_w <= rect_2_x:
        return False
    elif rect_1_y >= rect_2_y + rect_2_h:
        return False
    elif rect_1_y + rect_1_h <= rect_2_y:
        return False
    else:
        return True


def check_rectangle(first_red_tile_inner, second_red_tile_inner, arr_rect_to_check) -> tuple[bool, int]:
    # idea: create inner rectangle which does not have an overlap with any edge
    # Note: Certain scenarios of red tile pairs might result in a wrong solution
    #       In these cases, the inner rectangle does not have an overlap with any edge but the rectangle is still
    #       outside the loop of tiles
    min_x = min(first_red_tile_inner[0], second_red_tile_inner[0])
    min_y = min(first_red_tile_inner[1], second_red_tile_inner[1])
    max_x = max(first_red_tile_inner[0], second_red_tile_inner[0])
    max_y = max(first_red_tile_inner[1], second_red_tile_inner[1])
    rect_size: int = (max_x - min_x + 1) * (max_y - min_y + 1)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    # Ignore small rectangles
    if width <= 2 or height <= 2:
        return False, rect_size
    # Create inner rectangle
    rect_1 = (min_x + 1, min_y + 1, width - 2, height - 2)
    # Check for overlap between inner rectangle and edges
    for rect_2 in arr_rect_to_check:
        if rectangle_intersects(rect_1, rect_2):
            return False, rect_size

    return True, rect_size


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    pos_red_tiles = []
    rect_to_check = []
    with open(filename) as file:
        for line in file:
            # 1.) For each red tile pair, compute rectangle and choose the highest value as solution
            line = line.replace("\n", "")
            parts = line.split(",")
            pos_red_tiles.append((int(parts[0]), int(parts[1])))

    # 2.) Compute all edges between two neighboring red tiles as rectangle
    for i in range(len(pos_red_tiles)):
        first_red_tile = pos_red_tiles[i]

        if i == len(pos_red_tiles) - 1:
            second_red_tile = pos_red_tiles[0]
        else:
            second_red_tile = pos_red_tiles[i + 1]

        min_x_outer = min(first_red_tile[0], second_red_tile[0])
        min_y_outer = min(first_red_tile[1], second_red_tile[1])
        max_x_outer = max(first_red_tile[0], second_red_tile[0])
        max_y_outer = max(first_red_tile[1], second_red_tile[1])
        rect_to_check.append((min_x_outer, min_y_outer, max_x_outer - min_x_outer + 1, max_y_outer - min_y_outer + 1))

    max_rectangle_size = 0
    # 3.) Compute validity of rectangle for each red tile pair and choose the highest value of a valid rectangle as solution
    for i in range(len(pos_red_tiles)):
        first_red_tile = pos_red_tiles[i]
        for j in range(i + 1, len(pos_red_tiles)):
            second_red_tile = pos_red_tiles[j]

            is_valid, rectangle_size = check_rectangle(first_red_tile, second_red_tile, rect_to_check)
            if is_valid and rectangle_size > max_rectangle_size:
                max_rectangle_size = rectangle_size

    print("Solution Day 9 Part 2: ", max_rectangle_size)
