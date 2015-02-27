package mergesort 

import (
	"reflect"
	"testing"
	"fmt"
)

func TestMerge(t *testing.T) {
	a1 := []int{1,2,3,4}
	a2 := []int{5,6,7,8}
	res := merge(a1,a2)
	other := merge(a2,a1)
	fmt.Printf("Merge %#v & %#v, get %#v \n", a1, a2, res)
	if !reflect.DeepEqual(res, other) {
		t.Error(fmt.Sprintf("Merge %#v & %#v, get %#v or %#v \n", a1, a2, res, other))
	}
}

func TestSmallSort(t *testing.T) {
	a1:= []int{6,5}
	fmt.Printf("sort %#v to get %#v \n", a1, Sort(a1))
}


func TestSort(t *testing.T) {
	a1:= []int{56,345,34,77,22,23,90,1,2,8,88,75,6,5}
	fmt.Printf("sort %#v to get [%#v \n", a1, Sort(a1))
}

func TestLargerSort(t *testing.T) {
	in := []int{
		1986, 2003, 1927, 1959, 1957, 1988, 2009, 2003, 2003, 2003, 1945, 1941, 1917, 1953, 1991}
	fmt.Printf("sorting %#v\n gives %#v\n", in, Sort(in))
}
