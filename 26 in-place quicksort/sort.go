package sort


func Sort(a []int) []int {
	partition(a, 0, len(a)-1)
	return a

}

func partition(a []int, start, end int) {
		if start+1 >= end {
			// no need to separate when 0 or 1 element
			return 
		}
		
		s := start // new pivot element position to be
		for i:= start; i< end; i++ {
			if a[i] < a[end] {
				 a[i], a[s] = a[s], a[i]
				 s++
			} 
		}
		a[s], a[end] = a[end], a[s]
		partition(a, start, s-1)
		partition(a, s+1, end)
	}
