package main

import (
	"fmt"
	"strings"
)

func main() {
	var string1, string2 string
	fmt.Scanf("%v\n%v", &string1, &string2)
	fmt.Printf("* Longest Common Subsequence:\n")
	LongestCommonSubsequence(string1, string2).Show(string1, string2)
}

func LongestCommonSubsequence(P, Q string) lcs {
	A := make(subproblems, len(P))
	for i := 0; i < len(P); i++ {
		A[i] = make([]lcs, len(Q))
	}

	for i := 0; i < len(Q); i++ {
		for j := 0; j < len(P); j++ {
			if P[i] == Q[j] {
				if len(A.Get(i-1, j)) == len(A.Get(i, j-1)) {
					A[i][j] = append(A.Get(i-1, j-1), i, j)
					continue
				}
			}

			if len(A.Get(i-1, j)) > len(A.Get(i, j-1)) {
				A[i][j] = A.Get(i-1, j)
			} else {
				A[i][j] = A.Get(i, j-1)
			}
		}
	}
	return A[len(P)-1][len(Q)-1]
}

type subproblems [][]lcs

func (sp subproblems) Get(i, j int) lcs {
	if i < 0 || j < 0 {
		return lcs{}
	}
	return sp[i][j]
}

type lcs []int

func (l lcs) Show(P, Q string) {

	// show first string with highlightened symbols
	cur := -1
	fmt.Printf("~~~~~~~~~\n")
	for i := 0; i < len(l); i += 2 {
		fmt.Printf("%s%c",strings.Repeat("-", l[i]-cur-1), P[l[i]])
		cur = l[i]
	}
	fmt.Printf("\n")

	// show sec string
	cur = -1
	for i := 1; i < len(l); i += 2 {
		fmt.Printf("%s%c",strings.Repeat("-", l[i]-cur-1), Q[l[i]])
		cur = l[i]
	}
	fmt.Printf("\n")
	fmt.Printf("~~~~~~~~~\n")
}
