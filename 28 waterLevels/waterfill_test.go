package waterfill

import (
		"testing"
		"fmt"
)

func TestGetVolume(t *testing.T) {
	levels := []int{2,2,2,5,2,5,2,2,2}
	l, r := findHighestPointsInterval(levels, 0, len(levels)-1)
	fmt.Printf("We get two positions of %#v, %#v\n", l, r)	
}