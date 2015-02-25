package main

import "testing"

var p int

func TestParent(t *testing.T) {
	if -1 !=parent(0) {
		t.Error("parent of root is not -1")
	}

	if p= parent(1); p != 0 {
		t.Error("parent of root.left is not root: ",p)
	}

	if p= parent(2);p != 0 {
		t.Error("parent of root.right is not root, instead: ", p)
	}

}