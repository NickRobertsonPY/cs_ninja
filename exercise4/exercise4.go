package main

import (
	"fmt"
)

type pizza int

var x pizza = 5


func main() {
	fmt.Println(x)
	fmt.Printf("%T", x)
}
