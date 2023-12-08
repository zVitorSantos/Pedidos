<template>
    <nav class="navbar navbar-light bg-light fixed-top">
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
  
        <!-- Dropdown do Usuário -->
        <div class="dropdown">
          <button
            class="navbar-toggler bg-light navbar-light"
            type="button"
            id="dropdownMenuButton"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton">
            <li><router-link class="dropdown-item" to="/settings">Settings</router-link></li>
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
      const accessToken = localStorage.getItem('accessToken');
      await axios.post('http://127.0.0.1:5173/api/auth/logout', {}, {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      });
      localStorage.removeItem('accessToken');
      window.location.href = '/';
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
    .navbar-light .navbar-toggler-icon {
      background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3ccircle cx='12' cy='7' r='4'/%3e%3cpath d='M5.41 20.74a9 9 0 0 1 13.18 0'/%3e%3c/svg%3e");
    }
    .navbar-toggler:focus {
      outline: none;
    }
    .navbar-toggler:hover {
      border: 1px solid rgba(0, 0, 0, 0.1);
    }
    
  </style>