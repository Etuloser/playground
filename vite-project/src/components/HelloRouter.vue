<script setup lang="ts">
</script>

<template>
  <h1>Hello App!</h1>
  <p>
    <!--使用 router-link 组件进行导航 -->
    <!--通过传递 `to` 来指定链接 -->
    <!--`<router-link>` 将呈现一个带有正确 `href` 属性的 `<a>` 标签-->
  <ul>
    <li>
      <router-link to="/">Go to Home</router-link>
    </li>
    <li>
      <router-link to="/about">Go to About</router-link>
    </li>
    <li>
      <router-link to="/users/eles/posts/1">Go to User</router-link>
    </li>
  </ul>
  </p>
  <!-- 路由出口 -->
  <!-- 路由匹配到的组件将渲染在这里 -->
  <router-view></router-view>
</template>

<style scoped>
ul {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
}

li:not(:last-of-type) {
  margin-right: 1rem;
}

.router-link-active {
  color: orange;
}

.router-link-exact-active {
  color: crimson;
}
</style>
