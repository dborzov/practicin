package waterfill

import "fmt"

func GetVolume(levs []int) int {
	waters := make([]int, len(levs))
	markHighestInterval(levs, waters, 0, len(levs)-1)
	return computeVolume(levs, waters)
}



func computeVolume(levs, water []int) (out int) {
	for i:=0; i<len(levs); i++ {
		if water[i] > levs[i] {
			out += water[i] -levs[i]
		}
	} 
	return out
}


func findHighestPointsInterval(levs []int, idL, idR int) (l, r int) {
	idHigh := idL
	IndSecondHighest := idL
	for i:=idL+1; i<=idR; i++ {
		if levs[idHigh] <= levs[i] {
			idHigh = i
		} else {
			if levs[IndSecondHighest] < levs[i] {
				IndSecondHighest = i
			}
		}
	}

	if IndSecondHighest < idHigh {
		return IndSecondHighest, idHigh
	} else {
		return idHigh, IndSecondHighest		
	}
}

func markHighestInterval(levs, waters []int, idL, idR int) {
	if idR - idL <= 2 {
		// no puddles for intervals with 2 points or less
		return
	}

	l, r := findHighestPointsInterval(levs, idL, idR)
	min := levs[idL]
	if levs[idL] > levs[idR] {
		min = levs[idR]
	}

	for i:= l; l <= r; i++ {
		waters[i] = min
	}

	markHighestInterval(levs, waters, idL, l)
	markHighestInterval(levs, waters, r, idR)
} 
