package main

import (
	"fmt"
	"errors"
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
	// fmt.Printf("~~~ insert val %v to arr of len %v\n", val, pos)
	uh := append(*bh, val)

	for !(pos == 0) {
		if (uh[pos] < uh[parent(pos)]) {
			// new value already bubbled up to highest pos
			break
		}
		uh[parent(pos)], uh[pos] = uh[pos], uh[parent(pos)]
		pos = parent(pos) 
	}

	*bh = uh
}

func (bh *BinaryHeap) Pop() (int, error) {
	length := len(*bh)
	if (length== 0) {
		return 0, errors.New("Heap is empty, nothing to pop")
	}
	uh := *bh
	uh[0], uh[length -1] = uh[length -1], uh[0]
	*bh = uh[0:length-1]
	pos := 0
	for next:= bh.greaterChild(pos); next != pos ; {
		uh[next], uh[pos] = uh[pos], uh[next] 
		pos = next
		next = bh.greaterChild(pos)
	}
	return uh[length -1], nil
}

func parent(pos int) int {
	if pos == 0 {
		return -1
	}
	return (pos - 1) / 2
}

func (bh BinaryHeap) greaterChild(pos int) (swapto int) {
	leftCont := [2]int{pos, bh[pos]}
	rightCont := [2]int{pos, bh[pos]}

	if left:= 2*pos + 1; left < len(bh) {
		leftCont = [2]int{left, bh[left]}
	}

	if right:= 2*pos + 2; right < len(bh) {
		rightCont = [2]int{right, bh[right]}
	}

	greaterChild := &rightCont
	if leftCont[1] > rightCont[1] {
		greaterChild = &leftCont
	}

	if greaterChild[1] > bh[pos] {
		// we return index of a child greater than position
		return greaterChild[0]
	} 
	// no need to swap the positions, signal it with returning original pos
	return pos
}


func main() {
	bh := NewBinaryHeap()
	numbers := make([]int, CNT)
	for i := 0; i < CNT; i++ {
		numbers[i] = 1800 + rand.Intn(200)
		bh.Insert(numbers[i])
	}

	fmt.Printf("Here are the numbers we feed: %#v \n", numbers)

	for popped, err := bh.Pop(); err == nil; {
		fmt.Printf("Here is BH.Pop(): %#v \n", popped)
		popped, err = bh.Pop();
	}
	fmt.Printf("All the BH left: %#v \n", bh)
}
