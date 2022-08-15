package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	url := "https://sqlite.org/2022/sqlite-tools-linux-x86-3390200.zip"
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(resp)
}
