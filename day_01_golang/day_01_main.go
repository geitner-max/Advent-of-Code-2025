package main

import (
	"os"
	"path/filepath"
	"strings"

	day_01_part_one "puzzle.geitner-max.de/m/v2/day_01_golang/day_01_part_one"
	"puzzle.geitner-max.de/m/v2/day_01_golang/day_01_part_two"
)

const useExample bool = false

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	pathWd, _ := os.Getwd()
	filename := "input.txt"
	if useExample {
		filename = "example.txt"
	}

	path := filepath.Join(pathWd, filename)
	dat, err := os.ReadFile(path)
	check(err)
	lines := strings.Split(string(dat), "\n")
	day_01_part_one.PartOne(lines)
	day_01_part_two.PartTwo(lines)
}
