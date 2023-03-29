// profile.js
export var firstWord = "Hello";
export var LastWord = "World";

var one = 1;
var two = 2;
var three = 3;

// 应当优先使用此方法,方便观察输出变量
export { one, two, three };

// 函数也能导出
export function multiply(x, y) {
  return x * y;
}
