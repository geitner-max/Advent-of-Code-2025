import numpy as np

__author__ = "Maximilian Geitner"
__date__ = "08.12.2025"


def compute_distance(first_pos, second_pos):
    return np.sqrt(np.pow(first_pos[0] - second_pos[0], 2) + np.pow(first_pos[1] - second_pos[1], 2) + np.pow(
        first_pos[2] - second_pos[2], 2))


def replace_circuit(circuit, replace_value, replace_with):
    circuit_copy = [0] * len(circuit)
    for index_inner in range(len(circuit)):
        circuit_copy[index_inner] = replace_with if circuit[index_inner] == replace_value else circuit[index_inner]
    return circuit_copy


if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    shortest_connection_count = 1000
    if use_example:
        filename = "example.txt"
        shortest_connection_count = 10

    junction_boxes = []
    distances = []
    current_circuits = []
    with open(filename) as file:
        for line in file:
            # 1.) Create all junction boxes and initialize all circuits (one for each junction box)
            line = line.replace("\n", "")
            parts = line.split(",")
            junction_box = (int(parts[0]), int(parts[1]), int(parts[2]))
            junction_boxes.append(junction_box)
            current_circuits.append(len(junction_boxes) - 1)
    # 2.) Calculate all distances between two junction boxes and initialize matrix tracking connections
    distance_matrix = np.zeros((len(junction_boxes), len(junction_boxes)), dtype=float)
    connection_used = np.zeros((len(junction_boxes), len(junction_boxes)), dtype=int)
    for index_start, junction_box_start in enumerate(junction_boxes):
        for index_end, junction_box_end in enumerate(junction_boxes):
            if index_start < index_end:
                dist = compute_distance(junction_box_start, junction_box_end)
                distance_matrix[index_start, index_end] = dist
                distance_matrix[index_end, index_start] = dist
                distances.append((dist, index_start, index_end))
    # 3.) Sort distances in ascending order
    distances.sort(key=lambda tup: tup[0])
    # 4.) connect x shortest connections
    for index, (dist, index_first, index_second) in enumerate(distances):
        if index < shortest_connection_count:
            # merge circuits
            if current_circuits[index_first] != current_circuits[index_second]:
                current_circuits = replace_circuit(current_circuits, current_circuits[index_first],
                                                   current_circuits[index_second])
    # 5.) Count junction boxes for each remaining circuit
    remaining_circuits = list(set(current_circuits))
    remaining_circuit_count = [0] * len(remaining_circuits)
    for val in current_circuits:
        remaining_circuit_count[remaining_circuits.index(val)] += 1
    # 6.) Sort circuit size in descending order
    remaining_circuit_count.sort(reverse=True)
    solution = 1
    # 7.) Compute solution with the first three circuit sizes
    for i in range(3):
        solution *= remaining_circuit_count[i]
    print("Solution Day 8 Part 1: ", solution)
