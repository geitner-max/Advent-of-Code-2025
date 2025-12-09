__author__ = "Maximilian Geitner"
__date__ = "09.12.2025"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    pos_red_tiles = []
    with open(filename) as file:
        for line in file:
            # 1.) Read all red tile positions
            line = line.replace("\n", "")
            parts = line.split(",")
            pos_red_tiles.append((int(parts[0]), int(parts[1])))

    max_rectangle_size = 0
    # 2.) For each red tile pair, compute rectangle and choose the highest value as solution
    for i in range(len(pos_red_tiles)):
        first_red_tile = pos_red_tiles[i]
        for j in range(i + 1, len(pos_red_tiles)):
            second_red_tile = pos_red_tiles[j]
            min_x = min(first_red_tile[0], second_red_tile[0])
            min_y = min(first_red_tile[1], second_red_tile[1])
            max_x = max(first_red_tile[0], second_red_tile[0])
            max_y = max(first_red_tile[1], second_red_tile[1])
            rectangle_size = (max_x - min_x + 1) * (max_y - min_y + 1)
            if rectangle_size > max_rectangle_size:
                max_rectangle_size = rectangle_size
    print("Solution Day 9 Part 1: ", max_rectangle_size)
