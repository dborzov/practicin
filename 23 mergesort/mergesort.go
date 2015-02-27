package mergesort

func Sort(in []int) []int{
	if len(in) <2 {
		return in
	}
	mid := len(in) /2
	return merge(Sort(in[mid:]), Sort(in[:mid]))
}

// merge merges two sorted arrays into one sorted array
func merge(arr1, arr2 []int) []int {
	out := make([]int, len(arr1) + len(arr2))
	p1:=0
	p2:=0
	for p1 < len(arr1) && p2<len(arr2) {
		if arr1[p1] < arr2[p2] {
			out[p1+p2] = arr1[p1]
			p1++
		} else {
			out[p1+p2] = arr2[p2]
			p2++
		}
	}

	// leftover array slice is just copied
	l := arr2
	lp:= &p2
	if p1<len(arr1) {
		l= arr1
		lp = &p1
	}

	for *lp < len(l) {
		out[p1+p2] = l[*lp]
		*lp++
	}

	return out
}
