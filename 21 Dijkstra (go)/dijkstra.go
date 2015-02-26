package dijkstra

import "container/heap"

type tuple struct{
	v int // vertex index
	d float64 // distance to the vertex
}

type DistQueue []tuple
func (h DistQueue) Len() int           { return len(h) }
func (h DistQueue) Less(i, j int) bool { return h[i].d < h[j].d }
func (h DistQueue) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *DistQueue) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(tuple))
}

func (h *DistQueue) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Dijkstra(graph [][]float64, start int) []float64{
	// initialize with infinitely high values
	distances := make([]float64, len(graph))
	for i:=0; i<len(distances); i++ {
		distances[i]= 999999.0
	}
	distances[start] = 0.0

	// initialize priority queue
	pq := make(DistQueue, len(graph))
	pqp := &pq
	for i:=0; i<len(distances); i++ {
		pq[i] = tuple{
			v: i,
			d: distances[i],
		}
	}

	heap.Init(pqp)
	for pqp.Len() > 0 {
		p := pqp.Pop().(tuple)
		for j, d:= range graph[p.v] {
			if d==0.0 {
				// 0.0 denotes no edge
				continue
			}
			newDistance := p.d + d
			if newDistance < distances[j] {
				distances[j] = newDistance
				// pqp.UpdateKey(distances[p.Adjacent[j]],p.Adjacent[j]) 
			} 
		} 


	} 

	return []float64{}
}