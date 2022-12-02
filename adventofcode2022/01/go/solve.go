package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	// optionally, resize scanner's capacity for lines over 64K, see next example
	current := 0
	max := 0
	all := make([]int, 0)
	for scanner.Scan() {
		txt := scanner.Text()
		if txt == "" {
			fmt.Println("----")
			if current != 0 {
				all = append(all, current)
			}
			current = 0
		} else {
			intVar, err := strconv.Atoi(txt)
			check(err)
			fmt.Println(intVar)
			current += intVar
			if max < current {
				max = current
			}
		}
	}
	if current != 0 {
		all = append(all, current)
	}
	sort.Slice(all, func(i, j int) bool {
		return all[i] < all[j]
	})
	sum := 0
	for _, latest := range all[len(all)-3:] {
		sum += latest
	}

	fmt.Println(all[len(all)-3:])
	fmt.Printf("Max: %d\n", max)
	fmt.Printf("Sum of max 3: %d\n", sum)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
