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
import { ref, onMounted, defineAsyncComponent } from 'vue';
import axios from 'axios';

const NavBarAuth = defineAsyncComponent(() => import('../components/NavBarAuth.vue'));
const NavBarUnAuth = defineAsyncComponent(() => import('../components/NavBarUnAuth.vue'));
const HomeAuthenticated = defineAsyncComponent(() => import('../components/HomeAuth.vue'));
const HomeUnAuthenticated = defineAsyncComponent(() => import('../components/HomeUnAuth.vue'));
const Footer = defineAsyncComponent(() => import('../components/Footer.vue'));

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