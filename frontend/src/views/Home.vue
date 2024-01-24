<template>
  <main>
    <div v-if="isLoading">
      <!-- Mostrar algum tipo de spinner de carregamento aqui -->
      Loading...
    </div>
    <div v-else>
      <NavBarAuth v-if="isAuthenticated" :notifications="notifications.notifications" @notifications-checked="handleNotificationsChecked" />
      <NavBarUnAuth v-else />

      <HomeUnAuthenticated v-if="!isAuthenticated" />
      <HomeAuthenticated v-else />

      <Footer/>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted, defineEmits } from 'vue';
import axios from 'axios';

import NavBarAuth from '../components/NavBarAuth.vue';
import NavBarUnAuth from '../components/NavBarUnAuth.vue';
import HomeAuthenticated from '../components/HomeAuth.vue';
import HomeUnAuthenticated from '../components/HomeUnAuth.vue';
import Footer from '../components/Footer.vue';

let isAuthenticated = ref(false);
let isLoading = ref(true); 

let notifications = ref([]);

// Função para verificar notificações
const checkNotifications = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5173/api/auth/notifications', {
      headers: { 
        'Access-Control-Allow-Origin': '*',
        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
      }
    });
    if (response && response.data) {
      return response.data;
    }
  } catch (error) {
    console.error(error);
  }
  return [];
};

// Função para lidar com o evento notifications-checked
const handleNotificationsChecked = (newNotifications) => {
  notifications.value = newNotifications;
};

onMounted(async () => {
  try {
    const token = localStorage.getItem('accessToken');
    if (token) {
      try {
        const response = await axios.get('http://127.0.0.1:5173/api/auth/verify-token', { 
          headers: { 
            'Access-Control-Allow-Origin': '*',
            'Authorization': `Bearer ${token}` 
          }
        });

        if (response && response.data && 'logged_in_as' in response.data) {
          isAuthenticated.value = true;
        }
      } catch (error) {
        if (error.response && error.response.status === 401) {
          // Aqui você pode lidar com o erro 401 de maneira adequada
          console.log('Token inválido ou expirado');
        } else {
          // Outros erros (rede, servidor indisponível, etc.)
          console.error(error);
        }
      }
    }
  } finally {
    isLoading.value = false; 
  }
});
</script>