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
   return "hi";
}