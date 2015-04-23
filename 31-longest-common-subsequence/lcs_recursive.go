package main

import "fmt"

func main() {
	var P, Q string
	fmt.Scanf("%v\n%v", &P, &Q)
	fmt.Printf("Behold: %#s || %#s\n", P,Q)
	fmt.Printf("* Longest Common Subsequence: \"%s\" \n", LCS(P, Q))
}




func LCS(P, Q string) string {
	var memoizer = make(map[string]string)
	var subproblem func (i, j int) string
	subproblem = func(i, j int) string {
		if val, ok := memoizer[string(i) + "&" + string(j)]; ok {
			return val
		}

		if i < 0 || j < 0 {
			return ""
		}

		upper := subproblem(i-1, j)
		lefter := subproblem(i, j-1)
		backwards := subproblem(i-1, j-1)

		cur := lefter
		if len(upper) > len(lefter) {
			cur = upper
		}

		if P[i] == Q[j] {
			cur = backwards + string(P[i])
		}

		memoizer[string(i) + "&" + string(j)] = cur
		fmt.Printf("memoing [%v,%v]=%#s\n",P[:i+1],Q[:j+1],cur)
		return cur
	}

	return subproblem(len(P)-1, len(Q)-1)
}
