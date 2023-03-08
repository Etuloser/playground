import App from "./App.vue";
import router from "./router";
import ElementPlus from "element-plus";
import { createApp } from "vue";

const app = createApp(App);

app.use(router)
app.use(ElementPlus)
app.mount("#app")