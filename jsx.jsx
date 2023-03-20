// 变量声明，JSX会生成React元素
const element = <h1>Hello, world!</h1>;

// JSX中嵌入表达式使用大括号包裹
const name = "Eles";
const element1 = <h1>Hello, {name}</h1>;

// 也可以使用函数表达式
function formatName(user) {
  return user.firstName + " " + user.lastName;
}

const user = {
  firstName: "Zeng",
  lastName: "Yi",
  avatarUrl: "./avatar.jpg",
};

// JSX也可以是表达式
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}

const element2 = <h1>Hello, {getGreeting(user)}</h1>;
// 以通过使用引号，来将属性值指定为字符串字面量
const element3 = <div tabIndex="0"></div>;
// 也可以使用大括号，来在属性值中插入一个 JavaScript 表达式
// 可以使用闭合标签语法
const element4 = <img src={user.avatarUrl} />;

// 可以有很多子元素
const element5 = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
ReactDOM.render(element4, document.getElementById("jsx"));
