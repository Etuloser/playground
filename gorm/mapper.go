package gorm

type Curd[T any] struct {
	*Client
}

func (c *Curd[T]) Get(id int) *T {
	var t T
	c.DB.First(&t, id)
	return &t
}
func (c *Curd[T]) Create(entiry *T) {
	c.DB.Create(entiry)
}
func (c *Curd[T]) Put(entiry *T) {
	c.DB.First(entiry)
}

func (c *Curd[T]) Delete(entiry *T, id int) {
	c.DB.Delete(entiry, id)
}
