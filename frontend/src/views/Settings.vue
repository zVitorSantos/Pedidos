<template>
    <div>
        <NavBarAuth />
        
        <Settings />

        <Footer />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

import NavBarAuth from '../components/NavBarAuth.vue';
import Settings from '../components/Settings.vue';
import Footer from '../components/Footer.vue';

let isAuthenticated = ref(false);
const router = useRouter();

onMounted(async () => {
  try {
    const token = localStorage.getItem('accessToken');
    if (token) {
      const response = await axios.get('http://127.0.0.1:5173/api/auth/verify-token', { 
        headers: { Authorization: `Bearer ${token}` }
      });

      if (response.data && 'logged_in_as' in response.data) {
        isAuthenticated.value = true;
      } else {
        router.push('/login');
      }
    } else {
      router.push('/login');
    }
  } catch (error) {
    console.error(error);
    router.push('/login');
  }
});
</script>

<style>
/* Add your custom styles here */
</style>
