package main

import (
	"bufio"
	"fmt"
	"os"
	// "github.com/argusdusty/Ferret"
)

var line []byte
var isPrefix bool
var i = 0

var Converter = ferret.UnicodeToLowerASCII

func main() {
	// open input file
	f, err := os.Open("../Datasets/300words.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	Words := make([]string, 0)
	r := bufio.NewReader(f)
	for err == nil && !isPrefix {
		i++
		line, isPrefix, err = r.ReadLine()
		s := string(line)
		fmt.Println(i, s)
		Words = append(Words, s)
	}

	// SearchEngine := ferret.New(Words, Words, SongPopularities, func(s string) []byte { return []byte(s) })

}
