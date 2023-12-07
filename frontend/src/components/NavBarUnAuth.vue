<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container-fluid" style="height: 2.5rem;">
        <!-- Logo -->
        <a class="navbar-brand" href="#">Navbar</a>
  
        <!-- Busca -->
        <form class="d-flex input-group w-auto">
          <input
            type="search"
            class="form-control rounded"
            placeholder="Search"
            aria-label="Search"
            aria-describedby="search-addon"
          />
          <span class="input-group-text border-0" id="search-addon">
            <i class="fas fa-search"></i>
          </span>
        </form>
  
        <!-- Botões de Login e Registro -->
        <div>
          <button class="btn btn-primary" type="button" @click="goToLogin">
            Login
          </button>
          <button class="btn btn-secondary" type="button" @click="goToRegister">
            Register
          </button>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  const goToLogin = () => {
    router.push('/login');
  };
  
  const goToRegister = () => {
    router.push('/register');
  };
  </script>
  
  <style scoped>
  .navbar {
    background-color: #f8f9fa;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px; 
    z-index: 1030;
    display: flex;
    align-items: center;
    }
    .container-fluid {
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
    /* height: 100vh; */
    /* display: flex; */
    /* justify-content: center; */
    /* align-items: center; */
    }
  </style>