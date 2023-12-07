import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5173/api'

axios.interceptors.request.use(async (config) => {
  const token = localStorage.getItem('accessToken');
  const refreshToken = localStorage.getItem('refreshToken');

  if (token && refreshToken) {
    // Verifique se o token de acesso expirou
    const tokenExp = JSON.parse(atob(token.split('.')[1])).exp;
    if (Date.now() >= tokenExp * 1000) {
      // O token de acesso expirou, use o token de atualização para obter um novo token de acesso
      try {
        const response = await axios.post('/auth/refresh', {}, {
          headers: { Authorization: `Bearer ${refreshToken}` }
        });
        localStorage.setItem('accessToken', response.data.access_token);
        config.headers['Authorization'] = 'Bearer ' + response.data.access_token;
      } catch (error) {
        console.error(error);
      }
    }
  }

  return config;
}, (error) => {
  return Promise.reject(error);
});

const app = createApp(App);

app.use(router);

app.mount('#app');