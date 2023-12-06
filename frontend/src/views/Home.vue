<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import NavBar from '../components/NavBar.vue';
import Footer from '../components/Footer.vue';
import Home from '../components/Home.vue';
import HomeAuthenticated from '../components/HomeAuthenticated.vue';

let isAuthenticated = ref(false);

onMounted(async () => {
  try {
    const token = localStorage.getItem('accessToken');
    if (token) {
      const response = await axios.get('/verify-token', {
        headers: { Authorization: `Bearer ${token}` }
      });
      isAuthenticated.value = response.data.isAuthenticated;
    }
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <main>
    <NavBar/>

    <Home v-if="!isAuthenticated" />
    <HomeAuthenticated v-else />

    <Footer/>
  </main>
</template>