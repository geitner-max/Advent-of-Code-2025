package day_01_part_two

import (
	"fmt"
	"strconv"
	"strings"
)

func PartTwo(lines []string) {
	dial_pos := 50
	solution := 0

	for _, line := range lines {
		if strings.HasPrefix(line, "L") {
			value, _ := strconv.Atoi(line[1 : len(line)-1])
			for {
				if value > 0 {
					dial_pos -= 1
					value--
					if dial_pos == 0 {
						solution++
					} else if dial_pos < 0 {
						dial_pos = 99
					}
				} else {
					break
				}
			}
		} else if strings.HasPrefix(line, "R") {
			value, _ := strconv.Atoi(line[1 : len(line)-1])
			for {
				if value > 0 {
					dial_pos++
					value--
					if dial_pos == 100 {
						dial_pos = 0
						solution++
					}
				} else {
					break
				}
			}
		}
	}

	fmt.Println("Solution Day 1 Part 2: ", solution)
}
