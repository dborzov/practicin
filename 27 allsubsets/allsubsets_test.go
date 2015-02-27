package subsets

import (
	"testing"
	"fmt"
)

func TestSubsets(t *testing.T) {
	m:= Set([]int{1,4,6})
	fmt.Printf("   set: %#v\nsubsets:%#v\n", m, m.Subsets())
}