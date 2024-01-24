<template>
    <nav class="navbar navbar-light bg-light fixed-top">
      <div class="container-fluid d-flex justify-content-between align-items-center" style="height: 2.5rem;">
        <!-- Logo -->
        <a class="navbar-brand" href="/">V-System</a>
  
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

        <div class="d-flex align-items-center">
          <!-- Dropdown de Notificações -->
          <div
            class="dropdown me-3"
            @mouseover="animateIcon('notification')"
            @mouseleave="stopAnimation('notification')"
          >
            <button
              type="button"
              id="notificationDropdown"
              aria-expanded="false"
              style="background: none; border: none; position: relative;"
              :class="animateNotification ? 'animate__animated animate__pulse' : ''"
            >
              <i class="fas fa-bell fa-lg text-dark"></i>
              <span
                class="badge bg-warning text-dark"
                v-if="notifications && notifications.length > 0"
                style="position: absolute; top: -5px; right: -10px; border-radius: 50%; font-size: 0.6rem; padding: 5px; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center;"
              >
                {{ notifications.length }}
              </span>
            </button>
            <ul class="dropdown-menu dropdown-menu-start dropdown-menu-lg" aria-labelledby="notificationDropdown">
              <li v-for="notification in notifications" :key="notification.id">
                <a class="dropdown-item" href="#" @click="openModal(notification)">
                  {{ notification.text }} 
                </a>
              </li>
              <li v-if="notifications.length === 0">
                <a class="dropdown-item" href="#">
                  No notifications
                </a>
              </li>
            </ul>
          </div>
    
          <!-- Dropdown do Usuário -->
          <div
            class="dropdown"
            @mouseover="animateIcon('user')"
            @mouseleave="stopAnimation('user')"
          >
            <button
              type="button"
              id="dropdownMenuButton"
              aria-expanded="false"
              style="background: none; border: none;"
              :class="animateUser ? 'animate__animated animate__pulse' : ''"
            >
              <i class="fas fa-user fa-lg text-dark"></i>
            </button>
            <ul class="dropdown-menu dropdown-menu-start" aria-labelledby="dropdownMenuButton">
              <li><router-link class="dropdown-item" to="/settings">Settings</router-link></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#" @click="handleLogout">Logout</a></li>
            </ul>
          </div>

          <!-- Modal -->
          <div class="modal fade" id="userApprovalModal" tabindex="-1" aria-labelledby="userApprovalModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="userApprovalModalLabel">User Approval</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" v-if="selectedNotification && selectedNotification.value">
                  User: {{ selectedNotification.value.user_id }}
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-success" @click="approveUser">Approve</button>
                  <button type="button" class="btn btn-danger" @click="rejectUser">Reject</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  import { ref, onMounted, onUnmounted } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { Modal } from 'bootstrap';
  
  export default {
    props: {
      notifications: {
        type: Array,
        default: () => [],
      },
      onNotificationsChecked: {
        type: Function,
        default: function(newNotifications) {
          this.notifications = newNotifications;
        },
      },
    },

    setup(props, { emit }) {
      const router = useRouter();
      let notifications = ref([]);
      let intervalId = null;
      const animateNotification = ref(false);
      const animateUser = ref(false);
      let selectedNotification = ref(null);
  
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
  
      async function checkNotifications() {
        try {
          const accessToken = localStorage.getItem('accessToken');
          const response = await axios.get('http://127.0.0.1:5173/api/auth/notifications', {
            headers: {
              Authorization: `Bearer ${accessToken}`
            }
          });
          notifications.value = response.data.notifications;
          emit('notifications-checked', notifications.value); 
        } catch (error) {
          console.error(error);
        }
      }
  
      function handleNotificationClick(notification) {
        router.push(`/user/${notification.user_id}`);
      }
  
      const animateIcon = (icon) => {
        if (icon === 'notification') {
          animateNotification.value = true;
        } else if (icon === 'user') {
          animateUser.value = true;
        }
      };
  
      const stopAnimation = (icon) => {
        if (icon === 'notification') {
          animateNotification.value = false;
        } else if (icon === 'user') {
          animateUser.value = false;
        }
      };
  
      const setupDropdownHover = () => {
        var dropdown = document.querySelectorAll('.dropdown');
        dropdown.forEach(function(curDropdown) {
          curDropdown.addEventListener('mouseover', function() {
            this.classList.add('show');
            this.querySelector('.dropdown-menu').classList.add('show');
          });
          curDropdown.addEventListener('mouseout', function() {
            this.classList.remove('show');
            this.querySelector('.dropdown-menu').classList.remove('show');
          });
        });
      };

      onMounted(async () => {
        setupDropdownHover();
        await checkNotifications();

        // Mova o modal para o final do body uma vez quando o componente é montado
        var myModalElement = document.getElementById('userApprovalModal');
        document.body.appendChild(myModalElement);
      });

      const openModal = (notification) => {
        selectedNotification.value = notification;
        console.log(selectedNotification.value);
        var myModalElement = document.getElementById('userApprovalModal');
        var myModal = new Modal(myModalElement);
        myModal.show();

        // Mova o modal para o final do body
        document.body.appendChild(myModalElement);
      };

      onUnmounted(() => {
        document.removeEventListener('shown.bs.modal', function (event) {
          document.body.appendChild(event.target);
        }, false);
      });

      const closeModal = () => {
        var myModal = Modal.getInstance(document.getElementById('userApprovalModal'));
        myModal.hide();
      };
  
      const approveUser = async () => {
        try {
          const accessToken = localStorage.getItem('accessToken');
          const response = await axios.post(`http://127.0.0.1:5173/api/auth/approve_user/${selectedNotification.value.user_id}`, {}, {
            headers: {
              Authorization: `Bearer ${accessToken}`
            }
          });
          console.log(response.data.message);
          closeModal();
        } catch (error) {
          console.error(error);
        }
      };

      const rejectUser = async () => {
        try {
          const accessToken = localStorage.getItem('accessToken');
          const response = await axios.post(`http://127.0.0.1:5173/api/auth/reject_user/${selectedNotification.value.user_id}`, {}, {
            headers: {
              Authorization: `Bearer ${accessToken}`
            }
          });
          console.log(response.data.message);
          closeModal();
        } catch (error) {
          console.error(error);
        }
      };
  
      return {
        handleLogout,
        checkNotifications,
        handleNotificationClick,
        animateIcon,
        stopAnimation,
        setupDropdownHover,
        openModal,
        closeModal,
        approveUser,
        rejectUser,
        closeModal,
        notifications,
        animateNotification,
        animateUser,
        selectedNotification
      }
    },
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
    justify-content: space-between;
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

    @keyframes pulse {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.1);
    }
    100% {
      transform: scale(1);
    }
    }

    .animate__animated.animate__pulse {
      animation-name: pulse;
      animation-duration: 0.5s;
    }
    .dropdown-menu {
    left: auto !important;
    right: 0;
    }
    .dropdown-menu-lg {
    width: 300px; 
      }

    .modal {
      z-index: 1050 !important;
    }
    .modal-backdrop {
      z-index: 1040 !important;
    }
  
</style>