package mergesort

func Sort(a []int) []int {
	if len(a) < 2 {
		return a
	}
	mid := len(a)/2
	return merge(Sort(a[:mid]), Sort(a[mid:]))
} 


func merge(l, r []int) []int {
	out := make([]int, len(r) + len(l))
	var pl, pr int
	for {
		if pl == len(l) {
			return append(out[:pl+pr],r[pr:]...)
		}
		if pr == len(r) {
			return append(out[:pl+pr],l[pl:]...)
		}

		if (l[pl] > r[pr]) {
			out[pl+pr] = r[pr]
			pr++
		} else {
			out[pl+pr] = l[pl]
			pl++
		}
	}
}