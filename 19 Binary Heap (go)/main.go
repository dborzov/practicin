package main

import (
	"fmt"
	"math/rand"
)

type BinaryHeap []int

const (
	CNT = 100
)

func NewBinaryHeap() BinaryHeap {
	return BinaryHeap(make([]int, 0))
}

func (bh *BinaryHeap) Insert(val int) {
	pos := len(*bh)
	fmt.Printf("~~~ insert val %v to arr of len %v\n", val, pos)
	uh := append(*bh, val)

	for !(pos == 0) {
		if (uh[pos] > uh[parent(pos)]) {
			// new value already bubbled up to highest pos
			break
		}
		uh[parent(pos)], uh[pos] = uh[pos], uh[parent(pos)]
		pos = parent(pos) 
	}

	*bh = uh
}

func parent(pos int) int {
	if pos == 0 {
		return -1
	}
	return (pos - 1) / 2
}

func main() {
	bh := NewBinaryHeap()
	numbers := make([]int, CNT)
	for i := 0; i < CNT; i++ {
		numbers[i] = 1800 + rand.Intn(200)
		bh.Insert(numbers[i])
	}

	fmt.Printf("Here are the numbers we feed: %#v \n", numbers)
	fmt.Printf("Here is BH: %#v \n", bh)
}
