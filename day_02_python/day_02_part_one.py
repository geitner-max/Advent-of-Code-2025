
__author__ = "Maximilian Geitner"
__date__ = "02.12.2025"


def check_id_valid(number_str: str) -> bool:
    if len(number_str) % 2 == 0:
        start_index_middle = len(number_str) // 2
        for i in range(len(number_str) // 2):
            if number_str[i] != number_str[start_index_middle + i]:
                return True
        return False
    else:
        return True

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    # 1.) Read Input
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")

            number_ranges = list(filter(lambda text: len(text) > 0, line.split(",")))
            # 2.) Split input into number ranges
            for number_range in number_ranges:
                first_index = number_range.split("-")[0]
                last_index = number_range.split("-")[1]
                first_number = int(first_index)
                last_number = int(last_index)
                # 3.) Identify invalid numbers by comparing two sequences
                for number in range(first_number, last_number + 1):
                    if not check_id_valid(str(number)):
                        print(number)
                        solution += number

    print("Solution Day 2 Part 1: ", solution)
