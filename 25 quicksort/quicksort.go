package quicksort

func Sort(a []int) []int {
	if len(a) <2 {
		return a
	}
	c:= a[len(a)-1]
	l, g := split(a[:len(a)-1], c)
	return append(append(Sort(l),c),Sort(g)...)
}

func split(a []int, c int) ([]int, []int){
	var l, g []int
	for _, v := range a {
		if v < c {
			l = append(l,v)
		} else {
			g = append(g,v)
		}
	}
	return l, g
}