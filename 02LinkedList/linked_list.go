package main

import "fmt"

type Node struct {
	content string
	child   *Node
}

func (this *Node) Outline() string {
    new_string := " oops "
    if this.child != nil {
        new_string = this.child.Outline()
    }
    return "------node: " + this.content + "\n" + new_string
}

func (this *Node) Add(s string){
    if this.child != nil {
        this.child.Add(s)
    } else {
        new_node := new(Node)
        new_node.content = s 
        this.child = new_node
    }
}


func main() {
	linked_list := new(Node)
	linked_list.content = "Washington"
    linked_list.Add("Monica")
    linked_list.Add("Rubin")
	fmt.Printf("Behold the linked list rundown!\n")
    fmt.Printf(linked_list.Outline())
	fmt.Printf("hello, world\n")
}
