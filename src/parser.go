package main

import (
	"fmt"
	"os"
)

func main() {
	// Example of environment variable interpolation
	value := os.Getenv("CONFIG_VAR")
	fmt.Println("Config value:", value)
}
