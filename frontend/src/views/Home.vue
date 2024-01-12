<template>
  <main>
    <div v-if="isLoading">
      <!-- Mostrar algum tipo de spinner de carregamento aqui -->
      Loading...
    </div>
    <div v-else>
      <NavBarAuth v-if="isAuthenticated" />
      <NavBarUnAuth v-else />

      <HomeUnAuthenticated v-if="!isAuthenticated" />
      <HomeAuthenticated v-else />

      <Footer/>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

import NavBarAuth from '../components/NavBarAuth.vue';
import NavBarUnAuth from '../components/NavBarUnAuth.vue';
import HomeAuthenticated from '../components/HomeAuth.vue';
import HomeUnAuthenticated from '../components/HomeUnAuth.vue';
import Footer from '../components/Footer.vue';

let isAuthenticated = ref(false);
let isLoading = ref(true); 

// Função para verificar notificações
const checkNotifications = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5173/api/notifications', {
      headers: { Authorization: `Bearer ${localStorage.getItem('accessToken')}` }
    });
    if (response.data) {
      // Faça algo com as notificações aqui
    }
  } catch (error) {
    console.error(error);
  }
};

onMounted(async () => {
  try {
    const token = localStorage.getItem('accessToken');
    if (token) {
      const response = await axios.get('http://127.0.0.1:5173/api/auth/verify-token', { 
        headers: { Authorization: `Bearer ${token}` }
      });

      if (response.data && 'logged_in_as' in response.data) {
        isAuthenticated.value = true;
        await checkNotifications();
      }
    }
  } catch (error) {
    console.error(error);
  } finally {
    isLoading.value = false; 
  }
});
</script>