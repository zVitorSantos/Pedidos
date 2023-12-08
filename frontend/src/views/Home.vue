<template>
  <main>
    <NavBarAuth v-if="isAuthenticated" />
    <NavBarUnAuth v-else />

    <HomeUnAuthenticated v-if="!isAuthenticated" />
    <HomeAuthenticated v-else />

    <Footer/>
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

onMounted(async () => {
  try {
    const token = localStorage.getItem('accessToken');
    if (token) {
      const response = await axios.get('http://127.0.0.1:5173/api/auth/verify-token', { 
        headers: { Authorization: `Bearer ${token}` }
      });

      if (response.data && 'logged_in_as' in response.data) {
        isAuthenticated.value = true;
      }

    }
  } catch (error) {
    console.error(error);
  }
});
</script>