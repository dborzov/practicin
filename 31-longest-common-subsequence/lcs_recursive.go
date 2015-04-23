package main

import "fmt"

func main() {
	var string1, string2 string
	fmt.Scanf("%v\n%v", &string1, &string2)
	fmt.Printf("* Longest Common Subsequence: \"%s\" \n", LCS(string1, string2))
}


var memoizer = make(map[string]string)


func LCS(P, Q string) string {
	return subproblem(P,Q,len(P)-1, len(Q)-1)
}


func subproblem(P,Q string, i, j int) string {
	if val, ok := memoizer[string(i) + "&" + string(j)]; ok {
		return val
	}

	if i < 0 || j < 0 {
		return ""
	}

	upper := subproblem(P,Q, i-1, j)
	lefter := subproblem(P,Q, i, j-1)

	cur := lefter
	if len(upper) > len(lefter) {
		cur = upper
	}

	if P[i] == Q[j] {
		cur = cur + string(P[i])
	}

	memoizer[string(i) + "&" + string(j)] = cur
	return cur

}
