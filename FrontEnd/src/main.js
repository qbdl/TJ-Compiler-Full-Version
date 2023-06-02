import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'font-awesome/css/font-awesome.min.css'  // 使用图标库

createApp(App).use(store).use(router).mount('#app')
