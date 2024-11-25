package main

import (
	"net/http"
	"github.com/gin-gonic/gin"
)

type Item struct {
    ID    int  `json:"id"`
    Name  string  `json:"name"`
}

var items = []Item{
    {ID: 1, Name: "Galactic Goggles"},
    {ID: 2, Name: "Meteor Muffins"},
    {ID: 3, Name: "Alien Antenna Kit"},
	{ID: 4, Name: "Starlight Lantern"},
	{ID: 5, Name: "Quantum Quill"},
}

func main() {
	router := gin.Default()
	router.GET("/", greet)
	router.HEAD("/healthcheck", healthcheck)
	router.GET("/items", getItems)
	router.POST("/items", postItems)

	router.Run()
}


func getItems(c *gin.Context){
	c.IndentedJSON(http.StatusOK, items)
}

func postItems(c *gin.Context){
	var newItem Item
	newItem.ID = len(items) + 1
	if err := c.BindJSON(&newItem); err != nil {
        return
    }

    items = append(items, newItem)
    c.IndentedJSON(http.StatusCreated, newItem)
}

func greet(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, "Welcome, Go navigator, to the Anythink cosmic catalog.")
}

func healthcheck(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"status": "ok",
	})
}
