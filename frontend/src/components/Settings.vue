<template>
    <div class="container-fluid">
      <div class="row flex-nowrap">
        <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
          <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
            <router-link to="/" class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
              <span class="fs-5 d-none d-sm-inline">Menu</span>
            </router-link>
            <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
              <li class="nav-item">
                <router-link to="/settings/profile" class="nav-link align-middle px-0">
                <i class="fs-4 bi-house text-start"></i> <span class="ms-1 d-none d-sm-inline">Perfil</span>
                </router-link>
              </li>
              <!-- Add more links here for other settings sections -->
            </ul>
          </div>
        </div>
        <div class="col py-3">
          <!-- The settings content will be displayed here -->
          <router-view></router-view>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Settings',
    // Your component logic here
  }
  </script>
  
  <style scoped>
  .settings {
    display: flex;
  }
  
  .sidebar {
    width: 200px;
    padding: 1rem;
    border-right: 1px solid #ccc;
  }
  
  .content {
    flex-grow: 1;
    padding: 1rem;
  }
  </style>