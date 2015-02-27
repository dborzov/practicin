package mergesort

import (
	"testing"
	"fmt"
	"reflect"
)

func TestMerge(t *testing.T) {
	a1 := []int{1,2,3,4}
	a2 := []int{5,6,7,8}
	res := merge(a1,a2)
	other := merge(a2,a1)
	// fmt.Printf("Merge %#v & %#v, get %#v \n", a1, a2, res)
	if !reflect.DeepEqual(res, other) {
		t.Error(fmt.Sprintf("Merge %#v & %#v, get %#v or %#v \n", a1, a2, res, other))
	}
}