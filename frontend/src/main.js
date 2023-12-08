import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:5173/api'

axios.interceptors.response.use((response) => {
  return response;
}, async (error) => {
  const originalRequest = error.config;
  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true;
    const refreshToken = localStorage.getItem('refreshToken');
    try {
      const response = await axios.post('/auth/refresh', {}, {
        headers: { Authorization: `Bearer ${refreshToken}` }
      });
      localStorage.setItem('accessToken', response.data.access_token);
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access_token;
      return axios(originalRequest);
    } catch (err) {
      console.error(err);
    }
  }
  return Promise.reject(error);
});

const app = createApp(App);

app.use(router);

app.mount('#app');