import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5173/api'

const app = createApp(App);

app.use(router);

app.mount('#app');