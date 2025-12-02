
__author__ = "Maximilian Geitner"
__date__ = "02.12.2025"


# Part Two: Change repeated sequence check
def check_id_valid(number_str: str) -> bool:
    for sequence_len in range(1, len(number_str) // 2 + 1):
        if len(number_str) % sequence_len == 0:
            sel_seq = number_str[0:sequence_len]
            offset = sequence_len
            is_invalid = True
            for i in range(1, len(number_str) // sequence_len):
                if sel_seq != number_str[i * offset: i * offset + sequence_len]:
                    is_invalid = False
                    break
            if is_invalid:
                return False
    return True


if __name__ == '__main__':
    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    solution = 0
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")

            number_ranges = list(filter(lambda text: len(text) > 0, line.split(",")))

            for number_range in number_ranges:
                first_index = number_range.split("-")[0]
                last_index = number_range.split("-")[1]
                first_number = int(first_index)
                last_number = int(last_index)

                for number in range(first_number, last_number + 1):
                    if not check_id_valid(str(number)):
                        print(number)
                        solution += number

    print("Solution Day 2 Part 2: ", solution)
