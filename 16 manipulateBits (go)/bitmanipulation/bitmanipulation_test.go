package bitmanipulation

import "testing"

func TestGetBit1(t *testing.T) {
	v := BitInt(1)
	if v.GetBit(0) == false {
		t.Error("first bit of int32(1) yeilds 0")
	}
}


func TestGetBit2(t *testing.T) {
	v := BitInt(1)
	if v.GetBit(1) == true {
		t.Error("second bit of int32(1) yeilds 1")
	}

}