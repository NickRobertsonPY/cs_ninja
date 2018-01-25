package main

import (
	"fmt"
)

func main() {

	x := 50
	y := x << 1

	fmt.Printf("%d\t\t%b\t\t%x\n", x, x, x)
	fmt.Printf("%d\t\t%b\t\t%x", y, y, y)

}
