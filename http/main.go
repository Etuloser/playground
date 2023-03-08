package main

import (
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/upload", uploadHandler)

	log.Fatal(http.ListenAndServe(":30080", nil))
}
