package waterfill

import "testing"

func TestGetVolume(t *testing.T) {
	levels := []int{2,2,2,5,2,5,2,2,2}
	GetVolume(levels)	
}