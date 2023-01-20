package myptr

import (
	"fmt"
	"testing"

	"github.com/gookit/goutil/testutil/assert"
)

// 声明了一个变量name，它的类型是string
var name string

// 声明了一个变量ptr1，它的类型是*string，*string也是一种数据类型，用于存放string类型的地址
var ptr1 *string

// 声明了一个变量ptr2，它的类型是**string，即指向指针的指针类型，用于存放*sting类型的地址
var ptr2 **string

func SayHi(name string) {
	name = "Hi"
	fmt.Println(name)
}
func SayHiButPtr(name *string) {
	*name = "Hi"
	fmt.Println(*name)
}
func TestMyPtr(t *testing.T) {
	name = "Eles"
	ptr1 = &name
	fmt.Println(name) // Eles
	fmt.Println(ptr1) // 0x5f8330
	// 变量name的值是Eles，他的地址是0x5f8330，&name代表取变量name的地址，它的数据类型是*string
	assert.Equal(t, &name, ptr1)

	name = "Etuloser"  // 修改变量name的值
	fmt.Println(*ptr1) // *ptr1代表取指针指向内存地址的值
	fmt.Println(ptr1)  // 0x5f8330
	assert.Equal(t, *ptr1, "Etuloser")

	ptr2 = &ptr1
	fmt.Println(ptr2)
	fmt.Println(*ptr2)
	assert.Equal(t, *ptr2, ptr1)

	SayHi(name)       // Hi
	fmt.Println(name) // Etuloser
	assert.NotEqual(t, "Hi", name)
	// 可以看出，传参是值传递，相当于复制了一份name的值，它在函数内的变更并不会影响到name变量的值
	SayHiButPtr(ptr1) //
	fmt.Println(name)
	assert.Equal(t, "Hi", name) // 这里可以看出name的值已经被修改成Hi了
}
