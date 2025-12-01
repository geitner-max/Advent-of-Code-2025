
__author__ = "Maximilian Geitner"
__date__ = "01.12.2025"

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    dial_pos = 50
    solution = 0
    # 1.) Read Input
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")

            if line.startswith('L'):
                line = line.replace('L', '')
                diff = int(line)

                for i in range(diff):
                    dial_pos -= 1
                    if dial_pos == 0:
                        solution += 1
                    if dial_pos < 0:
                        dial_pos += 100

            elif line.startswith('R'):
                line = line.replace('R', '')
                diff = int(line)
                dial_pos += diff
                while dial_pos >= 100:
                    solution += 1
                    dial_pos -= 100

    print("Solution Day 1 Part 2: ", solution)
