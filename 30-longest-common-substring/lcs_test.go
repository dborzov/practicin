package lcs

import (
	"fmt"
	"testing"
)

func TestLongestCommonString(t *testing.T) {
	fmt.Printf(" here here: %v \n", LongestCommonSubstring("ama", "ama"))
	fmt.Printf(" here here: %v \n", LongestCommonSubstring("dama", "ama"))
	fmt.Printf(" here here: %v \n", LongestCommonSubstring("amad", "ama"))
	fmt.Printf(" here here: %v \n", LongestCommonSubstring("amad", "ammmmmmmmmmmmma"))
	fmt.Printf(" here here: %v \n", LongestCommonSubstring("dadma", "ama"))
	fmt.Printf(" here here: %v \n", LongestCommonSubstring("dadmad", "ama"))
	fmt.Printf(" here here: %v \n", LongestCommonSubstring("dadmad", "xaxmxax"))
}
