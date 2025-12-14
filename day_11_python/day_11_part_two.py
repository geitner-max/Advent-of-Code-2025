__author__ = "Maximilian Geitner"
__date__ = "11.12.2025"


def add_to_list(node, visited_dac, visited_fft, count, current_list):
    for i in range(len(current_list)):
        n, dac, fft, c = current_list[i]
        if n == node and dac == visited_dac and fft == visited_fft:
            current_list[i] = (node, visited_dac, visited_fft, c + count)
            return current_list
    current_list.append((node, visited_dac, visited_fft, count))
    return current_list

if __name__ == '__main__':
    initial_node = "svr"
    final_state_node = "out"
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example_part_two.txt"

    solution = 0
    edges = {}

    with open(filename) as file:
        for line in file:
            # 1.) Read all red tile positions
            line = line.replace("\n", "")

            parts = line.split(":")
            start_node = parts[0]
            dest_nodes = parts[1].strip().split(" ")
            edges[start_node] = dest_nodes


    to_evaluate = [(initial_node, False, False, 1)]
    # follow all flows to out
    # in each iteration, calculate next possible movement and record if path has visited dac and/or fft already
    while len(to_evaluate) > 0:
        next_to_evaluate = []
        for entry in to_evaluate:
            current_node, has_visited_dac, has_visited_fft, count = entry
            for next_node in edges[current_node]:
                if next_node == final_state_node:
                    if has_visited_dac and has_visited_fft:
                        solution += count
                else:
                    if next_node == "dac":
                        next_to_evaluate = add_to_list(next_node, True, has_visited_fft, count, next_to_evaluate)
                    elif next_node == "fft":
                        next_to_evaluate = add_to_list(next_node, has_visited_dac, True, count, next_to_evaluate)
                    else:
                        next_to_evaluate = add_to_list(next_node, has_visited_dac, has_visited_fft, count, next_to_evaluate)
        to_evaluate = next_to_evaluate

    print("Solution Day 11 Part 2: ", solution)
