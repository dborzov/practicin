package bfs

var visited = make(map[*Node]bool)

// BreadthFirstSearch applies visit() function to each node
func BreadthFirstSearch(root *Node, visit func(*Node)) {
	visit(root)
  visited[root] = true
	queue := NewQueue(0)
	for _, n := range root.Adjacent() {
		queue.Push(n)
	}

  for n := queue.Pop(); n !=nil; {
    for _, a := range n.Adjacent() {
    _, in := visited[a]
    if !in {
        visit(a)
        visited[a] := true
        queue.Push(a)
      }
    }
  }
}
