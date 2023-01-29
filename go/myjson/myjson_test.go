package myjson

import (
	"encoding/json"
	"fmt"
	"log"
	"testing"
)

type Message struct {
	Name string
	Body string
	Time int64
}

func TestMyJson(t *testing.T) {
	m := Message{"Alice", "Hello", 1294706395881547000}
	fmt.Println(m)
	b, err := json.Marshal(m)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(b))
}
