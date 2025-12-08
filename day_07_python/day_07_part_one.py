__author__ = "Maximilian Geitner"
__date__ = "07.12.2025"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0

    column_numbers = []
    start_pos = None
    tachyon_column_indices = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            # 1.) Find starting position
            if start_pos is None:
                start_pos = line.find('S')
                tachyon_column_indices = [False] * len(line)
                tachyon_column_indices[start_pos] = True
            else:
                next_tachyon_column_indices = [False] * len(tachyon_column_indices)
                # 2.) Compute tachyon positions in the next row for each remaining row
                for column_index in range(len(tachyon_column_indices)):
                    # 3. Count each split and apply new tachyons after split
                    if line[column_index] == '^' and tachyon_column_indices[column_index]:
                        solution += 1
                        # left split
                        if column_index >= 1:
                            next_tachyon_column_indices[column_index - 1] = True
                        # right split
                        if column_index + 1 < len(line):
                            next_tachyon_column_indices[column_index + 1] = True
                    else:
                        if tachyon_column_indices[column_index]:
                            next_tachyon_column_indices[column_index] = True
                tachyon_column_indices = next_tachyon_column_indices

    print("Solution Day 6 Part 1: ", solution)
