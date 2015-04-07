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

func Generate(length int) []string {
	return generate(0, length)
}

func generate(count int, length int) []string {
	var result []string
	if length > 0 {
		result = append(result, concatinateEach("(", generate(count+1, length-1))...)
	}
	if length > 0 && count > 0 {
		result = append(result, concatinateEach(")", generate(count-1, length-1))...)
	}

	if len(result) == 0 && count == 0 {
		return []string{""}
	}
	return result
}

func concatinateEach(prefix string, set []string) []string {
	var out []string
	for _, s := range set {
		out = append(out, fmt.Sprint(prefix, s))
	}
	return out
}
