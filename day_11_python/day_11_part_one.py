__author__ = "Maximilian Geitner"
__date__ = "11.12.2025"


if __name__ == '__main__':
    initial_node = "you"
    final_state_node = "out"
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

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

    to_evaluate = [initial_node]
    # follow all flows to out
    while len(to_evaluate) > 0:
        next_to_evaluate = []
        for current_node in to_evaluate:
            for next_node in edges[current_node]:
                if next_node == final_state_node:
                    solution += 1
                else:
                    next_to_evaluate.append(next_node)
        to_evaluate = next_to_evaluate

    print("Solution Day 11 Part 1: ", solution)
