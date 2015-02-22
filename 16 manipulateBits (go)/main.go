package main

import (
	"github.com/dborzov/bitmanipulation"
	"fmt"
)

func main() {
	i := bitmanipulation.BitInt(44)
	fmt.Printf("Behold 4: %s \n", i.String())
}