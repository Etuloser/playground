package mymap

import (
	"fmt"
	"testing"
)

func TestMyMap(t *testing.T) {
	// 声明一个map
	mymap := make(map[string]string)
	// 使用map
	mymap["hello"] = "hi"
	mymap["123"] = "321"

	// v为值, ok为键判断
	v, ok := mymap["hi"]
	fmt.Println(v, ok)

	// range map拿到的是键值对
	for i, x := range mymap {
		fmt.Println(i, x)
	}
}

