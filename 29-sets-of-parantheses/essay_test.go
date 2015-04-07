package parenthesis

import (
	"fmt"
	"testing"
)

func TestBalanced(t *testing.T) {
	if Balanced("()") == false {
		t.Error("Shows () as not balanced")
	}

	if Balanced("((") == true {
		t.Error("Shows (( as balanced")
	}

	if Balanced("(())") == false {
		t.Error("Shows (( as balanced")
	}

	if Balanced("(()))") == true {
		t.Error("Shows (( as balanced")
	}

	if Balanced("()()()") == false {
		t.Error("Shows (( as balanced")
	}
}

func TestGenerate(t *testing.T) {
	fmt.Printf("~~~~~~~~~\n")
	fmt.Print(Generate(6))
	fmt.Printf("\n~~~~~~~~~\n")
}
