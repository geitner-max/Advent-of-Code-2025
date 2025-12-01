package day_01_part_one

import (
	"fmt"
	"strconv"
	"strings"
)

func PartOne(lines []string) {
	dial_pos := 50
	solution := 0

	for _, line := range lines {
		if strings.HasPrefix(line, "L") {
			value, _ := strconv.Atoi(line[1 : len(line)-1])
			dial_pos -= value
			for {
				if dial_pos < 0 {
					dial_pos += 100
				} else {
					break
				}
			}
			if dial_pos == 0 {
				solution += 1
			}
		} else if strings.HasPrefix(line, "R") {
			value, _ := strconv.Atoi(line[1 : len(line)-1])
			dial_pos += value
			for {
				if dial_pos >= 100 {
					dial_pos -= 100
				} else {
					break
				}
			}
			if dial_pos == 0 {
				solution += 1
			}
		}
	}

	fmt.Println("Solution Day 1 Part 1: ", solution)
}
