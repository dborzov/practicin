package dijkstra

import ("testing")

const (
	Seattle iota
	SF
	NY
	Waterloo
)

func TestDijkstra(t testing.T) {
	var graph [4][4]float64
	graph[Seattle] = [...]float64{0,2,0,6}
	graph[SF] = [...]float64{2,0,7,0}
	graph[NY] = [...]float64{0,7,0,1}
	graph[Waterloo] = [...]float64{6,0,1,0}
	
	f := Dijkstra(graph, Waterloo)
	fmt.Printf("distance matrix from Waterloo: %#v \n", f)
}