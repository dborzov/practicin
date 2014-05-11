package main

import (
    "fmt"
)


type BinaryTreeNode interface {
  Left() *BinaryTreeNode
  Right() *BinaryTreeNode
  GetValue() int
}

func main() {
  BinaryTree := GetBinaryTree()
  _, isSearchTree := checkNode(BinaryTree)

  fmt.Println('isSearchTree: ', isSearchTree)

}

func checkNode(t *BinaryTree) int, bool {
  left_value, fail := checkNode(t.Left())
  if fail && left_value > t.GetValue() {
    return nil, true
  }

  right_value, fail := checkNode(t.Right())
  if fail && right_value < t.GetValue() {
    return nil, true
  }

  return right_value , false
}
