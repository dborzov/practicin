package mergesort



// Sort sort an array of ints
func Sort(in []int)[]int {
	return sort(in)

}

// merges 2 sorted arrays into one
func merge(a1 []int, a2 []int) []int {
	out := make([]int, len(a1) + len(a2))
	p1:=0
	p2:=0
	for p1 < len(a1) && p2 < len(a2) {
		if a1[p1] < a2[p2] {
			out[p1+p2] = a1[p1]
			p1++
		} else {
			out[p1+p2] = a2[p2]
			p2++
		}
	}

	leftover := &p2
	leftArray := a2
	if p1 < len(a1) {
		leftover = &p1
		leftArray = a1
	}


	for *leftover < len(leftArray) {
		out[p1+ p2] = leftArray[*leftover]
		*leftover++		
	}
	return out
}




func sort(a []int) []int{
	if len(a) <2 {
		return a
	}

	mid := len(a) /2
	return merge(sort(a[:mid]), sort(a[mid:]))
}
