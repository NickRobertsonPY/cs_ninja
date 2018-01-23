package main

import (
	"fmt"
)

type pizza int

var x pizza
var y int


func main() {
	x = 5
	y = int(x)
	fmt.Println(y)
	fmt.Printf("%T", y)
}
