package main

type Node struct {
	left, right *Node
	value       int
}

func (n Node) Left() *Node {
	return n.left
}

func (n Node) Right() *Node {
	return n.right
}

func (n Node) GetValue() int {
	return n.value
}

func GetBinaryTree() *Node {
	return &Node{
		value: 23,
	}
}
