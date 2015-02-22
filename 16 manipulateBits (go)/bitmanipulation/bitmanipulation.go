package bitmanipulation

type BitInt int32


func (x BitInt) GetBit(n uint32) bool{
	if n>31 {
		return false
	}
	m:= n & (1 << n)
	if m == 0 {
		return false
	} else {
		return true
	}
}

func (x BitInt) String() string {
	out := "["
	for i:=uint32(0); i<32; i++ {
		if x.GetBit(i) {
			out = out + "1"
		} else {
			out = out + "0"
		}
	}
	out = out + "]"
    return out;
}