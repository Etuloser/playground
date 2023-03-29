// JavaScript函数组件，它接收唯一带有数据的 “props”（代表属性）对象与并返回一个 React 元素
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
// 还可以使用 ES6 的 class 来定义组件，和上面是等价的
// class Welcome extends React.Component {
//   render() {
//     return <h1>Hello, {this.props.name}</h1>;
//   }
// }
// React元素也可以是用户自定义的组件, 注意组件名称必须以大写字母开头
const element = <Welcome name="Sara" />;
// 组合组件
function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("component"));
