package dijkstra


func Dijkstra(graph [][]float64, start int) []float64{
	pq.Add(start, distances[start])


	// initialize with infinitely high values
	distances := make([]float64, len(graph))
	for i:=0; i<len(distances); i++ {
		distances[i]= 999999.0
	}
	distances[start] = 0.0

	// initialize priority queue
	pq := PriorityQueue()
	for i:=0; i<len(distances); i++ {
		pq.Add(distances[i],i)
	}

	for !pq.IsEmpty() {
		p := pq.Pop()
		for j:= range p.Adjacent {
			newDistance := distances[p] + graph[p.Adjacent[j]]
			if newDistance < distances[p.Adjacent[j]] {
				distances[p.Adjacent[j]] := newDistance
				pq.UpdateKey(distances[p.Adjacent[j]],p.Adjacent[j]) 
			} 
		} 


	} 

}