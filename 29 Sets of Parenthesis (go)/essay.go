package parenthesis

import "fmt"

// Part 1:
// “” -> true
// “(“ -> false
// “)” -> false
// “()” -> true
// “)(“ -> false
// “(())” -> true
// “()()” -> true
// “()(())” -> true
// “(“ -> true, false

func Balanced(input string) bool {
	stack := []byte{}
	for _, s := range []byte(input) {
		if s == byte('(') {
			stack = append(stack, byte('('))
		}
		if s == byte(')') {
			if len(stack) == 0 {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}

	if len(stack) == 0 {
		return true
	} else {
		return false
	}
}

// Part 2:
//
// 2 -> “()”
// 3 -> nil
// 4 -> “(())”, “()()”
// 5- > nil
// 6 -> “()()()”, “()(())”, “((()))”, “(()())”, “(())()”

type sequence struct {
	s     string
	count int // number of unclosed parethesises
}

func Generate(length int) []string {
	all := generate(0, length)
	var balanced []string
	for _, e := range all {
		if e.count == 0 {
			balanced = append(balanced, e.s)
		}
	}
	return balanced
}

func generate(count int, length int) []sequence {
	var result []sequence
	if length > 0 {
		result = append(result, concatinateEach("(", generate(count+1, length-1))...)
	}
	if length > 0 && count > 0 {
		result = append(result, concatinateEach(")", generate(count-1, length-1))...)
	}

	if len(result) == 0 && count == 0 {
		return []sequence{sequence{
			s:     "",
			count: 0,
		},
		}
	}

	return result
}

func concatinateEach(prefix string, set []sequence) []sequence {
	var out []sequence
	for _, seq := range set {
		new := sequence{
			s:     fmt.Sprint(prefix, seq.s),
			count: seq.count,
		}
		out = append(out, new)
	}
	return out
}
