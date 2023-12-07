<template>
    <div v-if="isVisible" class="notification" :class="type">
      {{ message }}
    </div>
  </template>

<script>
export default {
  data() {
    return {
      isVisible: false,
      message: '',
      type: 'info', // Default type
    };
  },
  methods: {
    showNotification(message, type = 'info') {
      this.isVisible = true;
      this.message = message;
      this.type = type;

      setTimeout(() => {
        this.hideNotification();
      }, 3000);
    },
    hideNotification() {
      this.isVisible = false;
      this.message = '';
    },
  },
};
</script>

<style scoped>
.notification {
position: fixed;
top: 20px; 
left: 50%;
transform: translateX(-50%);
padding: 10px;
background-color: #ff0000d7; 
color: #fff; 
z-index: 1000;
border: 1px solid black;
border-radius: 10px; 
}

.notification.error {
  background-color: rgba(228, 35, 35, 0.843)
}
.notification.success {
  background-color: #2fb62fd7;
}
.notification.info {
  background-color: #42429ed7;
}
</style>
