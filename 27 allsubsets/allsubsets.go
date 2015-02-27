package subsets

type Set []int

func (s Set) Subsets() []Set {
	if len(s) == 0 {
		// empty set has only itself as a subset
		return []Set{Set([]int{})}
	}
	sel := s[0]
	return append(cproduct(sel, Set(s[1:]).Subsets()), Set(s[1:]).Subsets()...)
}

func cproduct(mre int, to []Set) []Set {
	out := make([]Set, len(to))
	for i:=0; i< len(out); i++ {
		out[i] = append(to[i], mre)
	}
	return out
}