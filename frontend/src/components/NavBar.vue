<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container-fluid">
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
  
        <!-- Dropdown do Usuário -->
        <div class="dropdown">
          <button
            class="btn btn-secondary dropdown-toggle"
            type="button"
            id="dropdownMenuButton"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            User
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li><a class="dropdown-item" href="#">Profile</a></li>
            <li><a class="dropdown-item" href="#">Settings</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#" @click="handleLogout">Logout</a></li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  const handleLogout = async () => {
    try {
      await axios.post('http://127.0.0.1:5173/api/auth/logout');
      localStorage.removeItem('accessToken');
      window.location.href = '/login';
    } catch (error) {
      console.error('Error logging out', error);
    }
  };
  </script>
  
  <style scoped>
  .navbar {
    background-color: #f8f9fa;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1030;
  }
  </style>